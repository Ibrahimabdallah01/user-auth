from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, loginForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def homepage(request):
    return render(request, "userauthenticate/homepage.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    context = {"form": form}

    return render(request, "userauthenticate/register.html", context=context)


# login
def my_login(request):
    form = loginForm()

    if request.method == "POST":
        form = loginForm(request, data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "userauthenticate/my-login.html", context=context)


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "userauthenticate/dashboard.html")


# logout


def user_logout(request):
    auth.logout(request)

    return redirect("")
