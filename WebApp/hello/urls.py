from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("max", views.max, name="max"),
    path("<str:name>", views.greet, name="greet")
]