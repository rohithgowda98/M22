from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/" , methods=['POST' , 'GET'])

def leapyear():
	msg = ''
	if request.method == 'POST' and 'input_year' in request.form:
		Input_year = int(request.form.get('input_year'))
		if (Input_year % 4) == 0:
			if (Input_year % 100) == 0:
				if (Input_year % 400) == 0:
					msg = '{0} is a Leap year'.format(Input_year)
				else: 
					msg = '{0} is Not a Leap year'.format(Input_year)
			else: 
				msg = '{0} is a Leap year'.format(Input_year)
		else:
			msg = '{0} is Not a Leap year'.format(Input_year)
	
	return render_template("index.html",msg=msg)	

@app.route('/')
def index():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080)