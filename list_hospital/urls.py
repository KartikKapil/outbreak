from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('<str:data>', views.list_hospitals, name='list_hospitals'),
    path('search/', views.search, name='search'),
]
