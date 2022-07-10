from django.urls import path
from . import views

urlpatterns = [
    path("tutorial/", views.tutorial, name="tutorial"),
    path("tutorial/<int:pk>/", views.tutorial_detail, name="tutorial_detail"),
]