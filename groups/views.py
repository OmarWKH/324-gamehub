from django.shortcuts import render
from .models import Group, UserGroup, Instances, Blogpost
from gametest.models import Game, List
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.views.generic import CreateView, UpdateView, DetailView
from django.template import loader
import datetime


class IndexView(generic.ListView):
    template_name = 'groups/index.html'

    def get_queryset(self):
        return Group.objects.all()


class GroupDetail(generic.DetailView):
    model = Group
    template_name = 'groups/detail.html'


class GroupCreate(CreateView):
    model = Group
    fields = ['name', 'description', 'area', 'is_public', 'creator']

    def get_initial(self):
        return {'creator': self.request.user }

    def get_form(self, form_class):
        form = super(generic.CreateView, self).get_form(form_class)
        current_username = self.request.user.username
        form.fields['creator'].queryset = User.objects.filter(username=current_username)
        return form

class JoinGroup(CreateView):
    model = UserGroup
    template_name = 'groups/join.html'
    fields = ['user', 'group']

    def get_initial(self):
        return {'user': self.request.user,
                'group': self.kwargs['group_id']}

    def get_form(self, form_class):
        form = super(generic.CreateView, self).get_form(form_class)
        current_username = self.request.user.username
        form.fields['user'].queryset = User.objects.filter(username=current_username)
        return form

    success_url = reverse_lazy('groups:index')

class InstanceDetails(generic.DetailView):
    model = Instances
    pk_url_kwarg = "instance_id"
    template_name = 'groups/instance_detail.html'


class CreateInstanceGr(CreateView):

    model = Group
    fields = ['name', 'description', 'area', 'is_public', 'creator']

    def get_initial(self):
        return {'creator': self.request.user,
                }

    def get_form(self, form_class):
        form = super(generic.CreateView, self).get_form(form_class)
        current_username = self.request.user.username
        form.fields['creator'].queryset = User.objects.filter(username=current_username)
        return form




class CreateInstance(CreateView):

    model = Instances
    template_name = 'groups/createInstance.html'
    fields = ['group', 'instance', 'game', 'instance_location', 'time']

    def get_initial(self):
        # try:
        #     group = UserGroup.objects.get(user=self.request.user, group=self.kwargs['group_id'])
        # except:
        #     raise Http404
        now = datetime.datetime.now()

        return {'instance': self.kwargs['group_id'],
                'time': now.strftime("%Y-%m-%d %H:%M")}

    def get_form(self, form_class):
        form = super(generic.CreateView, self).get_form(form_class)
        x = UserGroup.objects.filter(user=self.request.user).values_list('group')
        y = List.objects.filter(user=self.request.user).values_list('game')
        form.fields['group'].queryset = Group.objects.filter(group_id__in=x)
        form.fields['instance'].queryset = Group.objects.filter(pk=self.kwargs['group_id'])
        form.fields['game'].queryset = Game.objects.filter(game_id__in=y)
        return form



class CreateBlogpost(CreateView):
    model = Blogpost
    template_name = 'groups/createBlogpost.html'
    fields = ['text', 'is_public', 'group', 'user', 'bp_time']

    def get_initial(self):
        # try:
        #     group = UserGroup.objects.get(user=self.request.user, group=self.kwargs['group_id'])
        # except:
        #     raise Http404

        now = datetime.datetime.now()
        return {'user': self.request.user,
                'group': self.kwargs['group_id'],
                'bp_time': now.strftime("%Y-%m-%d %H:%M")}


    def get_form(self, form_class):
        form = super(generic.CreateView, self).get_form(form_class)
        current_username = self.request.user.username
        x = UserGroup.objects.filter(user=self.request.user).values_list('group')
        form.fields['user'].queryset = User.objects.filter(username=current_username)
        form.fields['group'].queryset = Group.objects.filter(group_id__in=x)
        return form

class BlogpostDetails(DetailView):
    model = Blogpost
    pk_url_kwarg = "bp_id"
    template_name = 'groups/blogpost_detail.html'

def GroupBlogposts(request, group_id):
    group_id = int(group_id)
    gname = Group.objects.get(pk=group_id)
    all_bps = Blogpost.objects.all()
    template = loader.get_template('groups/blogpost_of_group.html')
    context = {
        'all_bps': all_bps,
        'group_id': group_id,
        'gname': gname,
    }

    return HttpResponse(template.render(context, request))

def GroupInstances(request, group_id):
    group_id = int(group_id)
    gname = Group.objects.get(pk=group_id)
    all_instances = Instances.objects.all()
    template = loader.get_template('groups/instance_of_group.html')
    context = {
        'all_instances': all_instances,
        'group_id': group_id,
        'gname': gname,
    }

    return HttpResponse(template.render(context, request))