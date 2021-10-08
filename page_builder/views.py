from django.shortcuts import render
from django.views.generic import TemplateView


class BuilderView(TemplateView):
    template_name = "builder/builder.html"
