from django.shortcuts import render
from groups.models import UserGroup, Group
from gametest.models import Game, List
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.sites.models import Site



def index(request, user_id):
    user_id = int(user_id)
    uname = User.objects.get(pk=user_id)
    all_groups = UserGroup.objects.all()
    all_lists = List.objects.all()
    template = loader.get_template('userpage/index.html')
    context = {
        'all_groups': all_groups,
        'user_id': user_id,
        'all_lists': all_lists,
        'uname': uname,
    }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(settings.LOGIN_URL)

    groups = Group.objects.all()
    all_lists = List.objects.all()
    all_games = Game.objects.all()
    template = loader.get_template('userpage/dashboard.html')
    context = {
        'groups': groups,
        'all_lists': all_lists,
        'all_games': all_games,
    }

    return HttpResponse(template.render(context, request))