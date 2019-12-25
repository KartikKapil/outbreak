from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital_Name
from django.template import loader
import urllib.request
import requests
import json

def index1(request):
	return render(request,'list_hospital/home.html',{})
def index(request,longi,lati):
	all_hospitals=Hospital_Name.objects.all()
	template=loader.get_template('list_hospital/index.html')
	dist=[]
	for hsp in all_hospitals:
		url='https://api.mapbox.com/directions-matrix/v1/mapbox/driving/'+str(longi)+','+str(lati)
		url+=";"+str(hsp.longi)+','+str(hsp.lati)
		url+="?access_token=pk.eyJ1IjoianJhdmkyNDgiLCJhIjoiY2p6ZWM2N2k2MDB4YTNocWZpY3pzaWxmdiJ9.Enc1s0Mal1UmnYm-tJqqyA"
		response = requests.get(url)
		data = response.json()
		dist.append(0);

	
	context={
	'all_hospitals':all_hospitals, 'dist':dist}
	#html=""
	#for hsp in all_hospitals:
	#	url='list_for_hospital/'+str(hsp.id)+'/'
	#	html+="<a href='"+url+"'>"+hsp.name+"</a><br>"

	return HttpResponse(template.render(context,request))

# Create your views here.
def listing(request):
	all_hospitals=Hospital_Name.objects.all()
	template=loader.get_template('list_hospital/index.html')
	context={
	'all_hospitals':all_hospitals,	}
	#html=""
	#for hsp in all_hospitals:
	#	url='list_for_hospital/'+str(hsp.id)+'/'
	#	html+="<a href='"+url+"'>"+hsp.name+"</a><br>"


	return HttpResponse(template.render(context,request))

def detail_hospital(request,hospital_id):
	return HttpResponse("<h3> this is hospital</h3>")