from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='detail'),
    url(r'^create/$', views.GroupCreate.as_view(), name='create'),
    url(r'^join/$', views.JoinGroup.as_view(), name='join'),

    url(r'^instance/(?P<instance_id>[0-9]+)$', views.InstanceDetails.as_view(), name='InstanceDetails'),
    url(r'^(?P<group_id>[0-9]+)/createInstance', views.CreateInstance.as_view(), name='CreateInstance'),
    url(r'^(?P<group_id>[0-9]+)/instances$', views.GroupInstances, name='GroupInstances'),


    url(r'^(?P<group_id>[0-9]+)/createBlogpost', views.CreateBlogpost.as_view(), name='CreateBlogpost'),
    url(r'^blogpost/(?P<bp_id>[0-9]+)$', views.BlogpostDetails.as_view(), name='BlogpostDetails'),
    url(r'^(?P<group_id>[0-9]+)/blogposts', views.GroupBlogposts, name='GroupBlogposts'),
    # url(r'^(?P<group_id>[0-9]+)/blogposts/all', views.GroupBlogpostsAll.as_view(), name='GroupBlogpostsAll'),
]