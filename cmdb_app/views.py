from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm, AddEquipmentForm
from .models import NetworkEquipment
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form_register = RegisterForm(request.POST)
        if form.is_valid():
            user = form_register.save()
            login(request, user)
            return redirect("login_page")
    else:
        form_register = RegisterForm()
    return render(request, "login_page.html", {"form_register": form_register})


def login_page(request):
    if request.method == "POST":
        form_login = AuthenticationForm(request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form_login = AuthenticationForm()
    return render(request, "login_page.html", {"form_login": form_login})


def logout(request):
    logout(request)
    return redirect("login_page")


def dashboard(request):
    equipments = NetworkEquipment.objects.all()

    return render(request, "dashboard.html", {"equipments": equipments})


def add_equimpent(request):
    if request.method == "POST":
        add_equimpent_form = AddEquipmentForm(request.POST)
        if add_equimpent_form.is_valid():
            equipment = add_equimpent_form.save()
            messages.success(request, "Equipment added successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "There was an error adding the equipment")
    else:
        add_equimpent_form = AddEquipmentForm()
    return render(
        request, "add_equipment.html", {"add_equipment_form": add_equimpent_form}
    )
