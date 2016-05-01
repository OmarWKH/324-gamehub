from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from userpage import views

def view_profile(request):
    return redirect("/userpage/")
