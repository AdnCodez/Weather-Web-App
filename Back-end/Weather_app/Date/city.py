import sqlite3
import os.path


# ls = []
city_lat = 0
city_long = 0
def fun(city_name):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "weatherDB.db")
    with sqlite3.connect(db_path) as db:
        global city_lat
        global city_long
        cursor = db.cursor()
        # print(cursor)
        # var = cursor.execute("""select * from worldcities WHERE Country == 'ma' AND City == '{}'""".format(city_name))
        var = cursor.execute("select * from popcitiesonly WHERE City == '{}'".format(city_name))
        for row in var:
          city_lat  = row[5]
          city_long = row[6]
    return city_lat, city_long


# print(float(fun('kenitra')[0]))