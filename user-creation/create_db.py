import sqlite3

with sqlite3.connect("users.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE users(name TEXT, age INTEGER, sex TEXT, year INTEGER, major TEXT)""")