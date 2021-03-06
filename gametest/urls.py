from django.conf.urls import url

from . import views

app_name = 'gametest'

# (0-9)+ or (?P<pk>\d+)
urlpatterns = [
	url(r'^mine/$', views.my_games, name='my_games'),
	url(r'^$', views.games_list, name='games_list'),
	url(r'^show/([0-9]+)$', views.game_details, name='game_details'),
	url(r'^create/$', views.manage_game, name='create_game'),
	url(r'^edit/(?P<id>\d+)$', views.manage_game, name='edit_game'),
	url(r'^user_list/(?P<id>\d+)$', views.user_list_game, name='user_list_game')
]
