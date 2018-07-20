import flask
from flask import request, jsonify
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for




app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = {
	"James":{
		"e-mail": "james@gmail.com",
		"password":"12345"	

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
		
			
		#if(request.form['username'] == data["user_1"]["username"] and request.form['password']  == data["user_1"]["password"]):
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


@app.route('/users')
def users():
	return render_template('Users.html')

@app.route('/admin')
def admin():
	return render_template('Admin.html')



		

app.run()



