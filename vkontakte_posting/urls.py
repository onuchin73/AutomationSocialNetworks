from django.urls import path

from . import views


urlpatterns = [
    path("", views.vkontakte_posting.as_view()),
]