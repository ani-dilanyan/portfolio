from django.urls import path

from . import views

app_name = "main_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ProgrammerDetailView.as_view(), name="details"),
    path("add_programmer/", views.add_programmer, name="add_programmer"),
    path("<int:programmer_id>/add_project/", views.add_project, name="add_project"),
]
