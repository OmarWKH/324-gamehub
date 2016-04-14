from django.shortcuts import render
from .forms import LogInForm, RegisterationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse
from django.core.context_processors import csrf


def login_user(request):
    form = LogInForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You have logged in successfully ")  # Redirect to a success page.
        else:
            return HttpResponse("Invalid Email or password")
    return render(request, "registration/LogInForm.html", {"form": form})


def register_user(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("You successfully registered!")
    args = {}
    args.update(csrf(request))
    args['form'] = RegisterationForm()
    return render(request, "registration/SignUpForm.html", args)
