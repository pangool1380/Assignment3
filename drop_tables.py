import sqlite3

conn = sqlite3.connect('employees.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE devices
          ''')

conn.commit()
conn.close()
