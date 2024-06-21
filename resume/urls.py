from django.urls import path
from . import views

urlpatterns = [
    path("", views.resume, name="resume"),
    path(
        "generate_resume_pdf/<int:id>/",
        views.generate_resume_pdf,
        name="generate_resume_pdf",
    ),
]
