from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm, AddEquipmentForm
from .models import NetworkEquipment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            login(request, user)
            return redirect("login_page")
    else:
        form_register = RegisterForm()
    return render(request, "register.html", {"form_register": form_register})


def login_page(request):
    if request.method == "POST":
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("dashboard")
        else:
            messages.error(request, "Login failed. Please check your credentials.")
    else:
        form_login = AuthenticationForm()
    return render(request, "login_page.html", {"form_login": form_login})


def logout_view(request):
    logout(request)
    return redirect("login_page")


@login_required
def dashboard(request):
    equipments = NetworkEquipment.objects.all()

    return render(request, "dashboard.html", {"equipments": equipments})


@login_required
def add_equimpent(request):
    if request.method == "POST":
        add_equimpent_form = AddEquipmentForm(request.POST)
        if add_equimpent_form.is_valid():
            add_equimpent_form.save()
            messages.success(request, "Equipment added successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "There was an error adding the equipment")
    else:
        add_equimpent_form = AddEquipmentForm()
    return render(
        request, "add_equipment.html", {"add_equipment_form": add_equimpent_form}
    )


@login_required
def update_equipment(request, id):
    equipment = NetworkEquipment.objects.get(id=id)
    if request.method == "POST":
        update_form = AddEquipmentForm(request.POST, instance=equipment)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Equipment updated successfully")
            return redirect("dashboard")
        else:
            messages.error(request, "There was an error updating the equipment")
    else:
        update_form = AddEquipmentForm(instance=equipment)
    return render(
        request,
        "update_equipment.html",
        {"update_form": update_form},
    )


@login_required
def delete_equipment(request, pk):
    equipment = NetworkEquipment.objects.get(pk=pk)
    if request.method == "POST":
        equipment.delete()
        return redirect("dashboard")
    else:
        return redirect("dashboard")


@login_required
def equipment_details(request, id):
    details = NetworkEquipment.objects.get(id=id)

    context = {
        "id": details.id,
        "device_name": details.device_name,
        "device_type": details.device_type,
        "host": details.host,
        "location": details.location,
        "port": details.port,
        "status": details.status,
    }

    return render(request, "equipment_detail.html", context)
