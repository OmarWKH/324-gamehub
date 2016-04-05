from django.shortcuts import render
from .forms import RegistrationForm


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          return render(request, "registration/SignUpSuccessForm.html")
    else:
        form = RegistrationForm()
    return render(request, "registration/SignUpForm.html", {"form": form})
