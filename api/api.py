from flask import Flask, flash, redirect, render_template, Response, request, session, abort, url_for, jsonify
import json


app = Flask(__name__)
app.config["DEBUG"] = True

data = {
	"James":{
		"e-mail": "james@gmail.com",
		"password":"12345"	

	}
}

all_Requests = {
	"Repair": {
	"NAME":"James",
	"DEPARTMENT": "Accounts",
	"MESSAGE":"PC has broken down"
	},
	"Repair": {
	"NAME":"Justine",
	"DEPARTMENT": "IT",
	"MESSAGE":"AC not functioning"
	},
	"Maintenance": {
	"NAME":"Hasifa",
	"DEPARTMENT": "IT",
	"MESSAGE":"Need network cables"
	}
}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	print request.form
	if request.method == 'POST':
		if request.form['username'] == 'admin' or request.form['password'] == 'admin':
			return redirect(url_for('admin'))
		
		if request.form['username'] in data:
			return redirect(url_for('users'))
		else:
			error = "Invalid credentials Please Register" 
			return redirect(url_for('register'))

	return render_template('login.html', error=error)

	


@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		if request.form['user_name'] in data:
			return redirect(url_for('login'))
		else:
			user = {
				
				"e-mail": request.form['email'],
				"password": request.form['password']
			
			}
			data[request.form['user_name']] = user
			return redirect(url_for('login'))
	return render_template('Register.html')

@app.route('/users', methods=['GET','POST','PUT'])
def users():
	return render_template('Users.html')

#------------CREATE USER REQUEST----------------
@app.route('/users/requests', methods=['POST'])
def add_users():
	form_options = {
	request.form['option']: {
		"DEPARTMENT": request.form['department'],
		"NAME": request.form['name'],
		"MESSAGE": request.form['message']	
	}	
	}
	all_Requests.update(form_options)
	return jsonify(form_options)
	
#-------GET ALL USERS' REQUESTS-----------------
@app.route('/users/requests', methods=['GET'])
def get_users():
	return jsonify(all_Requests)

#-------GET A SPECIFIC USER REQUEST--------------
@app.route('/users/requests/<id>', methods=['GET'])
def get_user(id):
	user_id = all_Requests.get(id)
	return jsonify(user_id)

#--------------UPDATE A USERS' REQUEST--------------
@app.route('/users/requests/<id>', methods=['PUT'])
def update_user(id):
	user_id = all_Requests.get(id)
	form_options = {
	request.form['option']: {
		"DEPARTMENT": request.form['department'],
		"NAME": request.form['name'],
		"MESSAGE": request.form['message']	
	}	
	}

	all_Requests.update(form_options)
	return jsonify(form_options)


@app.route('/admin')
def admin():
	return render_template('Admin.html')		

app.run(debug=True)


