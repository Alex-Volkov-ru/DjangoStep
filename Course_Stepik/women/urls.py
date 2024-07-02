from django.contrib import admin
from django.urls import path, re_path, register_converter

from women import views
from women import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path("archive/<year4:year>/", views.archive)
]