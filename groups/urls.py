from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # detail
    url(r'(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='detail'),

    # create
    url(r'^create/$', views.GroupCreate.as_view(), name='create'),

    # join
    url(r'^(?P<pk>[0-9]+)/join/$', views.JoinGroup.as_view(), name='join'),

    url(r'(?P<pk>[0-9]+)/users$', views.ShowUsers.as_view(), name='show'),
]