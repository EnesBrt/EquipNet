from pyexpat.errors import messages
from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.management import call_command
from .models import Equipments
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    View,
)
from .forms import UpdateEquipmentsForm, CreateEquipmentsForm
from equipments.management.commands.connection import Command


class EquipmentsListView(ListView):
    model = Equipments
    template_name = "equipments/index.html"
    context_object_name = "equipments"


class EquipmentsDetailView(DetailView):
    model = Equipments
    template_name = "equipments/equipment_detail.html"
    context_object_name = "equipment"
    title = "Default"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class EquipmentsUpdateView(UpdateView):
    model = Equipments
    form_class = UpdateEquipmentsForm
    template_name = "equipments/equipment_update.html"
    context_object_name = "equipment"
    success_url = reverse_lazy("equipments:equipments_list")


class EquipmentsCreateView(CreateView):
    model = Equipments
    form_class = CreateEquipmentsForm
    template_name = "equipments/equipment_create.html"
    context_object_name = "equipment"
    success_url = reverse_lazy("equipments:equipments_list")


class DeleteEquipmentsView(DeleteView):
    model = Equipments
    template_name = "equipments/equipment_delete.html"
    context_object_name = "equipment"
    success_url = reverse_lazy("equipments:equipments_list")


def connect_equipments(request):
    call_command("connection", "--connect")
    return redirect("equipments:equipments_list")


def disconnect_equipments(request):
    call_command("connection", "--disconnect")
    return redirect("equipments:equipments_list")
