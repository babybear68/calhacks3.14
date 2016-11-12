from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    n1 = int(request.form['text'])
    n2 = int(request.form['text1'])
    return str(n1 + n2)

if __name__ == '__main__':
    app.run()