from django.urls import path
from . import views

urlpatterns = [
    path("", views.resume, name="resume"),
    path("resume/<int:id>/", views.resume, name="resume"),
]
