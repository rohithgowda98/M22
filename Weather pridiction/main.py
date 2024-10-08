# Mandatory components to be imported
from flask import Flask, render_template, request
# To view the flask response, which contains json data
import json
# Used for fetching URLs
import urllib.request

# Name the current component
app = Flask(__name__)


# This route method binds URL only when submit button is clicked in the POST or GET method. This route URL will be mentioned in form action of html template.
@app.route('/getWeather', methods=['POST', 'GET'])
def weather():
    # check if the method is POST or not
    if request.method == 'POST':
        location = request.form['city']
    #not necessary as the Exception is handled if no exception give any default city name
    else:
        location = 'chennai'
    # Assign your api key generated to the new variable
    api = "e0b19566bba38f97d53743b5e55c8662"

    try:
        # call url with location and api key
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + location +
            '&appid=' + api).read()

        # convert the response into python dictionary
        responseData = json.loads(source)

        # store the data you needed in an array
        data = {
            "country_code": str(responseData['sys']['country']),
            "temp": str(responseData['main']['temp']) + 'k',
            "location": str(responseData['name']),
        }

        # pass the array to html template
        return render_template('index.html', data=data)
    # exception handling
    except (Exception):
        # pass the error message that need to be displayed in html template
        return render_template('index.html', error="Give the correct location")


# route method that need to be called on first hit to render empty html template
@app.route('/')
def index():
    return render_template('index.html')


# Mention the port where the flask app should run
app.run(host='0.0.0.0', port=8080)
