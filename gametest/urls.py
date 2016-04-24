from django.conf.urls import url

from . import views

# (0-9)+ or (?P<pk>\d+)
urlpatterns = [
	url(r'^$', views.games_list, name='games_list'),
	url(r'^show/([0-9]+)$', views.game_details, name='game_details'),
	url(r'^create/$', views.manage_game, name='create_game'),
	url(r'^create/(?P<id>\d+)$', views.manage_game, name='edit_game'),
	url(r'^user_list/(?P<id>\d+)$', views.user_list_game, name='user_list_game')
]
