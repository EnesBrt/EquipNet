from cmdb_app import views
from django.urls import path, include

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_equipment/", views.add_equimpent, name="add_equipment"),
    path(
        "equipment_detail/<int:id>/", views.equipment_details, name="equipment_detail"
    ),
    path(
        "update_equipment/<int:id>/",
        views.update_equipment,
        name="update_equipment",
    ),
    path(
        "dashboard/delete_equipment/<int:pk>/",
        views.delete_equipment,
        name="delete_equipment",
    ),
]
