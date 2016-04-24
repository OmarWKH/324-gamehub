from django.shortcuts import render
from .models import Group, UserGroup
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from django.views.generic import CreateView, UpdateView, DetailView



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
    
    # def get_initial(self):
    #     return { 'creator': self.request.user }
    #
    # def get_form(self, form_class):
    #     form = super(generic.CreateView, self).get_form(form_class)
    #     current_username = self.request.user.username
    #     form.fields['creator'].queryset = User.objects.filter(username=current_username)
    #     return form

class JoinGroup(CreateView):
    model = UserGroup
    template_name = 'groups/join.html'
    fields = ['user', 'group']

    def get_initial(self):
        return {'user': self.request.user}

    # def get_form(self, form_class):
    #     form = super(generic.CreateView, self).get_form(form_class)
    #     current_username = self.request.user.username
    #     form.fields['user'].queryset = User.objects.filter(username=current_username)
    #     return form

    success_url = reverse_lazy('groups:index')
