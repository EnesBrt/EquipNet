from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from accounts.models import CustomUser
import logging

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("equipments:equipments_list")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("equipments:equipments_list")
        else:
            print("User not found")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("accounts:login")
