from flask import Flask
from flask import request
from flask import render_template
import sqlite3

def decolon(st):
    result = [[]]
    ir = 0
    for i in range(len(st)):
        if st[i] == ';':
            continue
        elif st[i + 1] == ';':
            result[ir].append(st[i])
            result[ir] = ''.join(result[ir])
            result.append([])
            ir = ir + 1
        else:
            result[ir].append(st[i])
    return result[:len(result) - 1]


def encode(lst):
    result = chr(31).join(lst)
    result = result + chr(31)
    return result

app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template("user-form.html")

@app.route('/', methods=['POST'])
def create_user_post():
    name = request.form['name']
    year = request.form['year']
    age = request.form['age']
    gender = request.form['gender']
    major = decolon(request.form['major'])
    interest = decolon(request.form['interest'])
    personality = decolon(request.form['personality'])
    contact = request.form['contact']
    st = 'INSERT INTO users VALUES("' + name + '", "'+ year + '", ' + str(age) + ', "' + gender + '", "' + encode(major) + '", "' + encode(interest) + '", "' + encode(personality) + '", "' + contact + '")'

    with sqlite3.connect("users.db") as connection:
        c = connection.cursor()
        c.execute(st)

    return 'User ' + name + ' created successfully!'

if __name__ == '__main__':
    app.run()