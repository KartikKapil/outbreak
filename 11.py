import requests
import json
import pandas
import csv

def app2(lati,longi):
	url3="https://maps.googleapis.com/maps/api/place/textsearch/json?query=hospital&key=AIzaSyCrK_sJw_cGjdUkX5mHNyz2fxb0UKjg1ts&location="
	url3+=str(lati)+","+str(longi)
	response3=requests.get(url3)
	data3=response3.json()
	for j in range(20):
		address_pharmacy=data3["results"][j]["formatted_address"]
		name_pharmacy=data3["results"][j]["name"]
		pharmacy_longi=data3["results"][j]["geometry"]["location"]["lng"]
		pharmacy_lati=data3["results"][j]["geometry"]["location"]["lat"]
		url2="https://api.mapbox.com/directions-matrix/v1/mapbox/driving/"+str(pharmacy_longi)+','+str(pharmacy_lati)+';'
		url2+=str(longi)+","+str(lati)
		url2+="?access_token=pk.eyJ1IjoianJhdmkyNDgiLCJhIjoiY2p6ZWM2N2k2MDB4YTNocWZpY3pzaWxmdiJ9.Enc1s0Mal1UmnYm-tJqqyA"
		response2=requests.get(url2)
		data2=response2.json()
		print(data2["destinations"][0]['distance'])


def index1(lati,longi):
	l=['pharmacy','primary+health+care+center','goverment+hospitals']
	for j in l:
		url="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+str(j)+"&key=AIzaSyCrK_sJw_cGjdUkX5mHNyz2fxb0UKjg1ts&location="
		url+=str(lati)+","+str(longi)
		response=requests.get(url)
		data=response.json()
		for i in range(20):
			address=data["results"][i]["formatted_address"]
			name=data["results"][i]["name"]
			data_lati=data["results"][i]["geometry"]["location"]["lat"]
			data_longi=data["results"][i]["geometry"]["location"]["lng"]

			url2="https://api.mapbox.com/directions-matrix/v1/mapbox/driving/"+str(data_longi)+','+str(data_lati)+';'
			url2+=str(longi)+","+str(lati)
			url2+="?access_token=pk.eyJ1IjoianJhdmkyNDgiLCJhIjoiY2p6ZWM2N2k2MDB4YTNocWZpY3pzaWxmdiJ9.Enc1s0Mal1UmnYm-tJqqyA"

			
			response2=requests.get(url2)
			data2=response2.json()
			print(data2["destinations"][0]['distance'])


def check(disease,lati,longi):
	rows=[]
	filename="all_disease.csv"
	with open(filename,'r') as csvfile:
		csvreader=csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)

	for i in range(len(rows)):
		#print(rows[i][0])
		if(str(rows[i][0])==str(disease)):
	 		print("correctly found")
	 		print(rows[i][1])
	 		if((rows[i][1]=="acute") or (rows[i][1]=="acute/chronic") or (rows[i][1]=="chronic/acute")):
	 			print("still correct")
	 			index1(lati,longi)
	 		else:
	 			print("chronic one ")
	 			app2(lati,longi)


#check("Acne",28.62955,77.37343) 


def new(symptom,age,d_o_b,gender):
	symptoms=[101,175,50]
	with open("allsympotoms.json") as json_file:
		data=json.load(json_file)

	for i in range(len(data)):
		if(data[i]["Name"]==str(symptom)):
			symptoms.append(data[i]["ID"])

	url="https://healthservice.priaid.ch/diagnosis?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im91dGJyZWFrLnNpaEBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjM2MTMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIxMDkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiMTAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiQmFzaWMiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDIwLTAxLTEwIiwiaXNzIjoiaHR0cHM6Ly9hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNTc4Njg2NDI0LCJuYmYiOjE1Nzg2NzkyMjR9.6pdxgzfvBBuVM6Hc9LkBqCRcRgQV3U19mkwAgZ47yVk&language=en-gb&symptoms="+str(symptoms)+"&gender="+str(gender)+"&year_of_birth="+str(d_o_b)

	r=requests.get(url)

	predicted_disease=r.json()

	print(predicted_disease)


#new("Abdominal pain",15,2001,"male")



	

