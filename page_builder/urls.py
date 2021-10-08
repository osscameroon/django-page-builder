from django.contrib import admin
from django.urls import path
from page_builder.views import BuilderView

urlpatterns = [
    path('builder/', BuilderView.as_view(), name='builder'),
]
