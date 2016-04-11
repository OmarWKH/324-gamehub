from django.shortcuts import render
from .forms import UserForm


def registration_form(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "registration/SignUpSuccessForm.html")
    else:
        form = UserForm()
        return render(request, "registration/SignUpForm.html", {"form": form})
