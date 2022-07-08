from django.urls import path

from . import views


urlpatterns = [
    path("", views.avito_parser.as_view()),
]