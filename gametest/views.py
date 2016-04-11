from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormView
from django.forms import ModelForm

from .models import *

class GameForm(ModelForm):
		class Meta:
			model = Game
			exclude = ('game_id',)
			# fields = [field.name for field in Game._meta.get_fields()]


# Could add filters to parameters
def games_list(request):
	list = Game.objects.all()
	context = {'games_list': list}
	return render(request, 'gametest/games_list.html', context)

def game_details(request, id):
	game = get_object_or_404(Game, game_id=id)
	# game = Game.objects.get(game_id=id)
	# form = GameForm(request.GET or None)
	context = {'game': game}
	return render(request, 'gametest/game_details.html', context)

def create_game(request):
	form = GameForm(request.POST or None)
	context = {'form': form}
	if form.is_valid():
		form.save()
		return redirect('gametest:games_list')
	return render(request, 'gametest/game_form.html', context)

# def edit_game(request, id):
# 	game = get_object_or_404(Game, game_id=id)
# 	form = GameForm(request.POST or None)
# 	context = {'form': form, 'game': game}
# 	if form.is_valid():
# 		form.save()
# 		return redirect('gametest:games_list')
# 	return render(request, 'gametest/game_form.html', context)

# def delete_game(request, id):