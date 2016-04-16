from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.forms import ModelForm, inlineformset_factory
from django import forms

from django.contrib.auth.models import User
from .models import *

# a way to choose if game is boardgame or not without having to fill pieces
# edit_game doesn't show the existing instance of board_game
# need to add other game types
# merge create_game and edit_game

# filter games/find game
# delete game
# in user_list_game hide user field
# edit/delte user_list_game

# ignore comments of code down below (other comments are helpufl, hopefully)

class GameForm(ModelForm):

	# def __init__(self, *args, **kwargs):
	# 	super(GameForm, self).__init__(*args, **kwargs)
	# 	self.fields['is_boardgame'] = models.BooleanField(default=False) #default
	# 	if self.instance:
	# 		if BoardGame.objects.filter(game=self.instance).exists():
	# 			self.fields['is_boardgame'].default=True
	# 		#else:
	# 		#	self.fields['is_boardgame'].initial=False
	# 	#else:
	# 	#	self.fields['is_boardgame'].initial=False

	class Meta:
		model = Game
		exclude = () # ('game_id',)
		# include_hidden = True
		# fields = [field.name for field in Game._meta.get_fields()]


class BoardGameForm(ModelForm):
	class Meta:
		model = BoardGame
		exclude = ('game',)


class UserListForm(ModelForm):
	class Meta:
		model = List
		exclude = ('id',)


# Could add filters to parameters
def games_list(request):
	list = Game.objects.all()
	context = {'games_list': list}
	return render(request, 'gametest/games_list.html', context)

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

	# will add boardgame form only if this is a boardgame
	if BoardGame.objects.filter(game=game_instance).exists():
		boardgame_form = BoardGameForm(request.GET or None, instance=BoardGame.objects.get(game=game_instance))
		context['boardgame_form'] = boardgame_form

	return render(request, 'gametest/game_details.html', context)

#requere login
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

def create_game(request):
	game_instance = Game()
	game_form = GameForm(request.POST or None, instance=game_instance)

	# creating an inline formset for boardgame linked to the empty instance game_instance
	BoardGameFormSet = inlineformset_factory(Game, BoardGame, exclude=()) #('game_id',))
	bg_request = get_formset_data(request, 'bg')
	boardgame_formset = BoardGameFormSet(bg_request, instance=game_instance, prefix='bg')
	
	context = {
		'game_form': game_form,
		'boardgame_formset': boardgame_formset
	}

	if game_form.is_valid() and boardgame_formset.is_valid():
		game_form.save()
	 	boardgame_formset.save()
	 	return redirect('gametest:games_list')
	return render(request, 'gametest/game_form.html', context)

def edit_game(request, id):
	game_instance = get_object_or_404(Game, game_id=id)
	game_form = GameForm(request.POST or None, instance=game_instance)
	
	# creating a boardgame inline formset linked to the instance game_instance
	BoardGameFormSet = inlineformset_factory(Game, BoardGame, exclude=()) #('game_id',))
	bg_request = get_formset_data(request, 'bg')
	boardgame_formset = BoardGameFormSet(bg_request, instance=game_instance, prefix='bg')

	context = {
		'game_form': game_form,
		'boardgame_formset': boardgame_formset
	}

	# boardgame_formset = BoardGameFormSet(request.POST, instance=game_instance, prefix='bg')
	if game_form.is_valid() and boardgame_formset.is_valid():
		game_form.save()
	 	boardgame_formset.save()
	 	return redirect('gametest:games_list')
	return render(request, 'gametest/game_form.html', context)

# add management data to post request, needed for inline formsets (like boardgame_form above)
# inline formset can add multiple forms, which explains total, initial, max_num below
def get_formset_data(request, prefix):
	total = prefix+'-TOTAL_FORMS'
	initial = prefix+'-INITIAL_FORMS'
	max_num = prefix+'-MAX_NUM_FORMS'
	request_values = request.POST.copy()
	request_values[total] = '1'
	request_values[initial] = '0'
	request_values[max_num] = ''
	return request_values

# def delete_game(request, id):
