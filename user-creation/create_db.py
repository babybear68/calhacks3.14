import sqlite3

with sqlite3.connect("users.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE users(name TEXT, year TEXT, age INTEGER, gender TEXT, major TEXT, interest TEXT, personality TEXT, contact TEXT, labels TEXT)""")
