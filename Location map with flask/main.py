from flask import Flask, render_template
import json
import urllib.request 


app = Flask(__name__)

@app.route('/',methods=['POST','GET']) 
def details():
	location = input("Enter the location here: ")
	api_key = 'AQwhmdsNoAXIAMKQY6lWSTNt_2Gg5rgc63hYO4_hBps'

	try:
		source = urllib.request.urlopen('https://geocode.search.hereapi.com/v1/geocode?apikey='+api_key+'&q='+location).read()

        print(source)

		responseData = json.loads(source)

		data = {
			"latitute" : str(responseData['items'][0]['position']['lat']),
			"longitute" : str(responseData['items'][0]['position']['lng']),
		}

		return render_template('index.html',data=data,apikey=api_key)
	except (Exception):
		return render_template('index.html',error="Give the correct location") 	
	

@app.route('/')
def index():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080)