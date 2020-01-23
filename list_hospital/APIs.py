import requests
import json
import csv
import time

def acute(lati,longi):
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


def chronic(lati,longi):
	# l=['pharmacy','primary+health+care+center','goverment+hospitals']
	l=['clinic']
	result = []
	for j in l:
		url="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+str(j)+"&key=AIzaSyCrK_sJw_cGjdUkX5mHNyz2fxb0UKjg1ts&location="
		url+=str(lati)+","+str(longi)
		response=requests.get(url)
		data=response.json()
		destinations = []
		for i in range(20):
			lat = data["results"][i]["geometry"]["location"]["lat"]
			lng = data["results"][i]["geometry"]["location"]["lng"]
			destinations.append({'point': {'latitude': lat, 'longitude': lng}})
		request_body = {
			'origins': [
				{
					'point': {'latitude': lati, 'longitude': longi}
				}
			],
			'destinations': destinations
		}

		header = {
			'Content-Type': 'application/json'
		}

		jsonData = json.dumps(request_body)

		res = requests.post('https://api.tomtom.com/routing/1/matrix/sync/json?key=2hvVqQig2YrGgunrjXUNJiaWXAGCEHg9&routeType=fastest&travelMode=car', data = jsonData, headers = header)
		res = res.json()
		for i in range(20):
			result.append({
				'name': data["results"][i]["name"],
				'address': data["results"][i]["formatted_address"],
				'distance': res['matrix'][0][i]['response']['routeSummary']['lengthInMeters']/1000
			})
		# time.sleep(3)
	return result


def check(disease,lati,longi):
	rows=[]
	filename="diseases.csv"
	with open(filename,'r') as csvfile:
		csvreader=csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)

	for i in range(len(rows)):
		if(str(rows[i][0])==str(disease)):
	 		print("correctly found")
	 		print(rows[i][1])
	 		if((rows[i][1]=="acute") or (rows[i][1]=="acute/chronic") or (rows[i][1]=="chronic/acute")):
	 			print("still correct")
	 			return chronic(lati,longi)
	 		else:
	 			print("chronic one ")
	 			return acute(lati,longi)
