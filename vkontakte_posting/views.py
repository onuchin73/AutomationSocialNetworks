from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import vkontakte_posting


class vkontakte_posting(ListView):
    model = vkontakte_posting
    template_name = "vkontakte_posting/vkontakte_posting.html"
