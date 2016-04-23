from django.shortcuts import render
from .models import UserGroup1, Group1, List1
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request, user_id):
    all_groups = UserGroup1.objects.all()
    all_lists = List1.objects.all()
    template = loader.get_template('userpage/index.html')
    user_id = int(user_id)
    context = {
        'all_groups': all_groups,
        'user_id': user_id,
        'all_lists': all_lists,
    }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/accounts/login/')

    return HttpResponse('test')