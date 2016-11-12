import sqlite3

with sqlite3.connect("events.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE users(name TEXT, num INTEGER, dt TEXT, type TEXT)""")