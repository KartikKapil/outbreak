from django.contrib import admin
from . import views
from django.urls import path

app_name="list_hospital"

urlpatterns=[
#basic page which will get loaded
	path('',views.index1,name="main_index"),
	path('<str:longi>,<str:lati>/',views.index,name='index'),
	path('list_for_hospital/',views.listing,name='list_for_hospital'),
	path('list_for_hospital/<int:hospital_id>/',views.detail_hospital,name='detail_view_hospital'),
]