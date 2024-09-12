import sqlite3

connection = sqlite3.connect('todo.db')

with connection:
    connection.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        );
    ''')

print("Base de datos inicializada.")
connection.close()
