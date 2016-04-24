from django.conf.urls import url
from . import views

app_name = 'userpage'

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.index, name='index'),
    url(r'^$', views.dashboard, name='dashboard')
]