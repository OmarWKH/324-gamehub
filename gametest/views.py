from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.forms import ModelForm, inlineformset_factory, modelform_factory
from django import forms

from django.contrib.auth.models import User
from .models import *

import logging
from datetime import datetime
logger = logging.getLogger('django')
# a way to choose if game is boardgame or not without having to fill pieces
# platform

# delete game
# in user_list_game hide user field
# edit/delte user_list_game

# ignore comments of code down below (other comments are helpufl, hopefully)

GAME_TYPES_MODELS = [BoardGame, CardGame, PhysicalGame, TabletopRpg, VideoGame]

class GameForm(ModelForm):
	class Meta:
		model = Game
		exclude = ()

class SimpleGameForm(ModelForm):
	class Meta:
		model = Game
		exclude = ('description', 'poster', )


class UserListForm(ModelForm):
	class Meta:
		model = List
		exclude = ('id',)


def games_list(request):
	search_instance = Game()
	search_form = SimpleGameForm(request.POST or None, instance=search_instance)

	if request.POST:
		search_query = request.POST.dict()
		request.POST = None
		
		del search_query['csrfmiddlewaretoken']
		for key, value in search_query.items():
			if (value == ''):
				del search_query[key]
		make_icontains(search_query, ['name', 'competitve_level', 'age_group'])

		list = Game.objects.filter(**search_query)
	else:
		list = Game.objects.all()

	forms_list = []
	for game in list:
		forms_list.append(SimpleGameForm(request.GET or None, instance=game))

	context = {
		'forms_list': forms_list,
		'search_form': search_form
	}

	if request.POST:
		return games_list(request)
	return render(request, 'gametest/games_list.html', context)

def make_icontains(query, keys):
	for key in keys:
		if key in query:
			query[key+'__icontains'] = query.pop(key)


def game_details(request, id):
	game_instance = get_object_or_404(Game, game_id=id)
	
	game_form = GameForm(request.GET or None, instance=game_instance)
	context = {'game_form': game_form}

	# list of players who listed the game, if any
	try:
		players_list = List.objects.filter(game=game_instance)
		context['players_list'] = players_list
	except DoesNotExist:
		pass

	# genre
	genres = []
	genre_records = Type.objects.filter(game=game_instance)
	for record in genre_records:
		genres.append(record.genre)
	context['genres'] = genres

	# adds game type forms for for all game types in GAME_TYPES_MODELS array (defined at the top)
	gametypes_forms = []
	for model in GAME_TYPES_MODELS:
		gametype_form = get_gametype_form(model, game_instance, request)
		if gametype_form:
			gametypes_forms.append(gametype_form)
	context['gametypes_forms'] =  gametypes_forms

	return render(request, 'gametest/game_details.html', context)

def get_gametype_form(GameType, game_instance, request):
	if GameType.objects.filter(game=game_instance).exists():
		GameTypeForm = modelform_factory(GameType, exclude=('game',))
		gametype_form = GameTypeForm(request.GET or None, instance=GameType.objects.get(game=game_instance))
		return gametype_form

def manage_game(request, id=None):
	if id:
		game_instance = get_object_or_404(Game, game_id=id)
	else:
		game_instance = Game()
	game_form = GameForm(request.POST or None, instance=game_instance)
	context = {'game_form': game_form}

	genres_formset = get_full_game_formset_or_empty(Type, game_instance, request)	
	gametypes_formsets = []
	for Model in GAME_TYPES_MODELS:
		formset = get_full_game_formset_or_empty(Model, game_instance, request)
		gametypes_formsets.append(formset)
	context['genres_formset'] = genres_formset
	context['gametypes_formsets'] = gametypes_formsets

	if request.method == 'POST':
		gametypes_formsets_are_valid = True
		for formset in gametypes_formsets:
			gametypes_formsets_are_valid = formset.is_valid()

		if game_form.is_valid() and genres_formset.is_valid() and gametypes_formsets_are_valid:
			game_form.save()
			for form in genres_formset:
				if form.instance.genre is not u'':
					form.instance.game_id = game_form.instance.game_id
					if form in genres_formset.deleted_forms:
						form.instance.delete()
					else:
						form.save()
			for formset in gametypes_formsets:
				formset.save()
			return redirect('gametest:games_list')

	return render(request, 'gametest/game_form.html', context)

def get_full_game_formset_or_empty(Model, game_instance, request):
		if request.method == 'POST':
			number_of_forms = Model.objects.filter(game=game_instance).count()
			if id and (number_of_forms > 0):
				return get_game_formset(Model, game_instance, request, number_of_forms, number_of_forms)
			else:
				return get_game_formset(Model, game_instance, request)
		else:
			return get_game_formset(Model, game_instance)

def get_game_formset(Model, game_instance, request=None, total_forms='1', initial_forms='0'):
	model_prefix = Model.type().lower()
	GameModelFormSet = inlineformset_factory(Game, Model, exclude=(), extra=1) #('game_id',))
	if request is None:
		return GameModelFormSet(instance=game_instance, prefix=model_prefix)
	else:
		if (model_prefix+'-TOTAL_FORMS') not in request.POST:
			request_with_data = get_formset_data(request, model_prefix, total_forms, initial_forms)
		else:
			request_with_data = request.POST
		model_formset = GameModelFormSet(request_with_data, instance=game_instance, prefix=model_prefix)
		return model_formset

# add management data to post request, needed for inline formsets (used for game types above)
# inline formset can add multiple forms, which explains total, initial, max_num below
def get_formset_data(request, prefix, total_forms='1', initial_forms='0'):
	total = prefix+'-TOTAL_FORMS'
	initial = prefix+'-INITIAL_FORMS'
	max_num = prefix+'-MAX_NUM_FORMS'
	request.POST = request.POST.copy()
	request.POST[total] = total_forms
	request.POST[initial] = initial_forms
	request.POST[max_num] = ''
	return request.POST


def user_list_game(request, id):
	game_instance = get_object_or_404(Game, game_id=id)
	current_user = request.user
	initial_values = {'game': game_instance, 'user': current_user}
	list_form = UserListForm(request.POST or None, initial=initial_values) # or None > field is required gone?! | initial works
	list_form.fields['user'].queryset = User.objects.filter(username=current_user.get_username())

	context = {'list_form': list_form}

	if list_form.is_valid():
		list_form.save()
		return redirect('gametest:games_list') # could: game_details, where users are shown
												# could: userpage, where games are shown
	return render(request, 'gametest/user_list_form.html', context)


# def delete_game(request, id):
