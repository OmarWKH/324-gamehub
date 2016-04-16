from django.shortcuts import render
from .models import Group, UserGroup
from django.views import generic
from django.views.generic import CreateView, UpdateView, DetailView


class IndexView(generic.ListView):
    template_name = 'groups/index.html'

    def get_queryset(self):
        return Group.objects.all()


class DetailView(generic.DetailView):
    model = Group
    template_name = 'groups/detail.html'


class GroupCreate(generic.CreateView):
    model = Group
    fields = ['name', 'description', 'area', 'is_public', 'creator']


class JoinGroup(generic.ListView):
    model = UserGroup
    template_name = 'groups/detail.html'
    # context_object_name = 'ug'
    # fields = ['id', 'user', 'group']

    def get_queryset(self):
        return UserGroup.objects.all()