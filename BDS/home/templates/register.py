import sqlite3
connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
cursor.execute('CREATE TABLE accounts (id INTEGER PRIMARY KEY, email TEXT, password TEXT)')
cursor.execute('INSERT INTO accounts (name, email) VALUES (?, ?)', ('John Doe', 'john.doe@example.com'))
cursor.execute('SELECT * FROM accounts')
rows = cursor.fetchall()
