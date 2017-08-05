import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS "
              "stuffToPlot"
              "(unix REAL, datestamp TEXT,"
              " keyword TEXT, value REAL)")


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.
               fromtimestamp(unix).
               strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('''
    INSERT INTO stuffToPlot
   (unix, datestamp, keyword, value)
   VALUES (?, ?, ?, ?)''',
              (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute('''
    SELECT * FROM stuffToPlot
    WHERE value=? AND unix>?
    ''', (3, 1501810619))

    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('''
    SELECT unix, value
    FROM stuffToPlot''')
    dates = []
    values = []
    for row in c.fetchall():
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-' )
    plt.show()

def del_and_update():
    c.execute('''
    SELECT *
    FROM stuffToPlot
    ''')
    print(50*'#')

    #updating all values that are == 3 to 99
    # c.execute('''
    # UPDATE stuffToPlot
    # SET value=?
    # WHERE value=?''',
    #           (99,3))
    # conn.commit()

    #reselecting data
    # c.execute('''
    # SELECT *
    # FROM stuffToPlot
    # ''')
    # [print(row) for row in c.fetchall()]

    c.execute('''
    DELETE
    FROM stuffToPlot
    WHERE value=?''',
              (99,))
    conn.commit()

    c.execute('''
    SELECT *
    FROM stuffToPlot
    ''')
    [print(row) for row in c.fetchall()]

# create_table()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
# read_from_db()

# graph_data()

del_and_update()

c.close()
conn.close()
