import sqlite3
import User

def decode(st):
    result = [[]]
    ir = 0
    for i in range(len(st)):
        if st[i] == chr(31):
            continue
        elif st[i + 1] == chr(31):
            result[ir].append(st[i])
            result[ir] = ''.join(result[ir])
            result.append([])
            ir = ir + 1
        else:
            result[ir].append(st[i])
    return result[:len(result) - 1]

def fetch(username):
    with sqlite3.connect("users.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM users")
        result = None
        while True:
            r = c.fetchone()
            if r == None:
                break
            if r[0] == username:
                result = r
                break
    if result == None:
        None
    else:
        return User(result[0], result[1], result[2], result[3], decode(result[4]), decode(result[5]), decode(result[6]), result[7])
