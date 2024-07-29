from django.contrib import admin
from django.urls import path, re_path, register_converter

from women import views
from women import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]