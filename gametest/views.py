from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.forms import ModelForm, inlineformset_factory
from django import forms
from django.views.generic import CreateView, UpdateView, DetailView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import *

# a way to choose if game is boardgame or not without having to fill pieces
# edit_game doesn't show the existing instance of board_game
# need to add other game types
# merge create_game and edit_game

# ignore comments of code down below (other comments are helpufl, hopefully)


class CreateGame(generic.CreateView):

	model = Game
	fields = ['name', 'description', 'poster', 'no_of_players', 'duration', 'no_of_sessions', 'age_group', 'competitve_level']
	success_url = reverse_lazy('gametest:games_list')

class EditGame(UpdateView):

	model = Game
	fields = ['name', 'description', 'poster', 'no_of_players', 'duration', 'no_of_sessions', 'age_group', 'competitve_level']
	success_url = reverse_lazy('gametest:games_list')


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



# Could add filters to parameters
def games_list(request):
	list = Game.objects.all()
	context = {'games_list': list}
	return render(request, 'gametest/games_list.html', context)

def game_details(request, id):
	game_instance = get_object_or_404(Game, game_id=id)
	
	game_form = GameForm(request.GET or None, instance=game_instance)
	context = {'game_form': game_form}

	# will add boardgame form only if this is a boardgame
	if BoardGame.objects.filter(game=game_instance).exists():
		boardgame_form = BoardGameForm(request.GET or None, instance=BoardGame.objects.get(game=game_instance))
		context['boardgame_form'] = boardgame_form

	return render(request, 'gametest/game_details.html', context)

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
