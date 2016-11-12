from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template("user-form.html")

@app.route('/', methods=['POST'])
def create_user_post():
	name = request.form['name']
	age = request.form['age']
	if request.form['sex'] == 'm':
		sex = 'Male'
	else:
		sex = 'Female'
	year = request.form['year']
	major = request.form['major']
	return 'User ' + name + ' created successfully!'

if __name__ == '__main__':
    app.run()