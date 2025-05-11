from django.urls import path
from . import views

app_name = "https_login"

urlpatterns = [
    path("", views.index, name="index"),
]
