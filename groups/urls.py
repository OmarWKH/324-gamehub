from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # detail
    url(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # create
    url(r'^create/$', views.GroupCreate.as_view(), name='create'),
]