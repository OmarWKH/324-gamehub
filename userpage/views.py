from groups.models import UserGroup, Group
from gametest.models import Game, List, Type
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from random import randint



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

    lst = []
    lst2 = []
    groups = Group.objects.all()
    all_lists = List.objects.all()
    all_games = Game.objects.all()
    all_types = Type.objects.all()

    # to find genres
    for gl in all_lists:
        if gl.user.id == request.user.pk:
            lst.append(gl.game.pk)

    for t in all_types:
        for g in lst:
            if g == t.game.game_id:
                lst2.append(t.genre)

    clst2 = len(lst2)
    rand = randint(0, clst2-1)
    genre = lst2[rand]

    template = loader.get_template('userpage/dashboard.html')
    context = {
        'groups': groups,
        'all_lists': all_lists,
        'all_games': all_games,
        'all_types': all_types,
        'genre': genre,
    }

    return HttpResponse(template.render(context, request))