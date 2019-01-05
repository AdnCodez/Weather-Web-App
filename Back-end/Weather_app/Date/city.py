import sqlite3
import os.path


def fun(city_name):
  ls = []
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  db_path = os.path.join(BASE_DIR, "cities.db")
  with sqlite3.connect(db_path) as db:

      cursor = db.cursor()
    
      var = cursor.execute("""select * from worldcities WHERE Country == 'ma' AND City == '{}'""".format(city_name))
      for row in var:
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[5])
        ls.append(row[6])
  return ls


print(fun('rabat'))
