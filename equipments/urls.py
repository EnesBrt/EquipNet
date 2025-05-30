from django.urls import path
from .views import (
    EquipmentsListView,
    EquipmentsDetailView,
    EquipmentsUpdateView,
    EquipmentsCreateView,
    DeleteEquipmentsView,
    connect_equipments,
    disconnect_equipments,
)

app_name = "equipments"

urlpatterns = [
    path("", EquipmentsListView.as_view(), name="equipments_list"),
    path("detail/<int:pk>/", EquipmentsDetailView.as_view(), name="equipment_detail"),
    path("update/<int:pk>", EquipmentsUpdateView.as_view(), name="equipment_update"),
    path("create/", EquipmentsCreateView.as_view(), name="equipment_create"),
    path("delete/<int:pk>", DeleteEquipmentsView.as_view(), name="equipment_delete"),
    path("connect/", connect_equipments, name="connect_equipments"),
    path("disconnect/", disconnect_equipments, name="disconnect_equipments"),
]
