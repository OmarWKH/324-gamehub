from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy

def view_profile(request):
    return render(request, 'userpage:dashboard')
