from django.urls import path
from rango import views
from django.shortcuts import render

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]