
import sqlite3

# connect to database or create it if it doesnt exist
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS "
              "stuffToPlot(unix REAL, datestamp TEXT,"
              "keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES("
              "123123112, '2016-01-01', 'Python', 5)")
    conn.commit() # ran every time you want to modify something
    c.close()
    conn.close()

create_table()
data_entry()
