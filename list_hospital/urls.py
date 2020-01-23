from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('<str:disease>', views.list_hospitals, name='list_hospitals'),
    path('search/', views.search, name='search'),
    path('symptoms/complaints/', views.take_symptoms, name='take_symptoms'),
    path('symptoms/confirmation/', views.confirmation, name='confirmation'),
    path('symptoms/interview/', views.interview, name='interview'),
]
