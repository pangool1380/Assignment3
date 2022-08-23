import sqlite3

conn = sqlite3.connect('employees.qlite')

c = conn.cursor()
c.execute ('''
           CREATE TABLE employees
           employee_id INTEGER PRIMARY KEY ASC,
           first_name VARCHAR(100) NOT NULL,
           last_name VARCHAR(100) NOT NULL,
           date_started DATETIME NOT NULL,
           type VARCHAR(6) NOT NULL,
           station_name VARCHAR(100) NOT NULL,
           station_id INTEGER NOT NULL,
           train_name VARCHAR(100) NOT NULL,
           train_id INTEGER NOT NULL 
              ''')


conn.commit()
conn.close()
