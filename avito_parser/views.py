from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import avito_parser


class avito_parser(ListView):
    model = avito_parser
    template_name = "avito_parser/avito_parser.html"
