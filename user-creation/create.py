from flask import Flask
from flask import request
from flask import render_template
import sqlite3

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
	st = 'INSERT INTO users VALUES("' + name + '", '+ str(age) + ', "' + sex + '", ' + str(year) + ', "' + major + '")'

	with sqlite3.connect("users.db") as connection:
		c = connection.cursor()
		c.execute(st)

	return 'User ' + name + ' created successfully!'

if __name__ == '__main__':
    app.run()