from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import main_page


class main_page(ListView):
    model = main_page
    template_name = "main_page/main_page.html"
