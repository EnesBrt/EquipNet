from cmdb_app import views
from django.urls import path, include

urlpatterns = [
    path("", views.login_page, name="login_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_equipment/", views.add_equimpent, name="add_equipment"),
]
