from flask import Flask
from flask import request
from flask import render_template
from Calculator import  *
import sqlite3

app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template("event-form.html")

@app.route('/', methods=['POST'])
def fetch_post():
	name = request.form['name']
	number = request.form['number']
	dt = request.form['datetime']
	ty = request.form['type']
	st = 'INSERT INTO events VALUES("' + name + '", '+ str(number) + ', "' + dt + '", ' + ty + '")'

	with sqlite3.connect("events.db") as connection:
		c = connection.cursor()
		c.execute(st)

	return 'Event ' + name + ' created successfully!'

def calculate_score(event, user):


if __name__ == '__main__':
    app.run()