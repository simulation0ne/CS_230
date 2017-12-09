from bottle import route, run, template, static_file, get, post, request

# Static routing for css
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root="./static")

# Index page with BMI form
@get('/')
def index():
	return template('index.html')

# Result page & calculates BMI info
@post('/calcBMI')
def calc_bmi():
	feet = request.forms.get('height-ft')
	inches = request.forms.get('height-in')
	weight = request.forms.get('weight')
	weight_method = request.forms.get('weight_method')
	if weight_method == "kg":
		weight = float(weight) * 2.2046226218
	height = (int(feet) * 12) + int(inches)
	weight = float(weight)
	height = int(height)
	bmi = (weight / (height*height)) * 703
	bmi = str(bmi)
	bmi = bmi[:4]
	bmi = float(bmi)
	if bmi <= 18.5:
		result = "underweight"
	elif bmi <= 24.9:
		result = "normal"
	elif bmi <= 29.9:
		result = "overweight"
	else:
		result = "obese"
	return template('result.html', bmi=bmi, result=result)


run(debug=True, reloader=True)