import datetime
import mysql.connector

CONFIG = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'employees',
}

cnx = mysql.connector.connect(**CONFIG)
cursor = cnx.cursor()

query = ("""SELECT first_name, last_name, hire_date
            FROM employees
            WHERE hire_date BETWEEN %s AND %s""")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(2999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()