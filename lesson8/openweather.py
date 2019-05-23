__author__ = 'Михайловский Василий Владимирович'

import os
import json
# import urllib.request
import requests
import urllib.parse
import sqlite3
from datetime import datetime

DIR = 'data'

with open(os.path.join(DIR, 'city.list.json'), 'r', encoding='UTF-8') as f1:
    cities = json.load(f1)
    f1.close()
with open(os.path.join(DIR, 'APPID.id'), 'r', encoding='UTF-8') as f2:
    appid = f2.readline()
    f2.close()

ask_city=input("Ведите город латиницей. например Saint Petersburg: ").lower()
try:
    city_index=[]
    for el in cities:
        if el.get("name").lower() == ask_city:
            city_index.append(cities.index(el))

    if len(city_index)>1:
        print("Найдены седующие города:")
        for ind, value in enumerate (city_index):
            print(f"{ind+1} - {cities[value]}")
        choose_city = input("Введите порядковый номер Вам нужного города из найденых: ")
        index_in_list = city_index[int(choose_city) - 1]
    else:
        index_in_list = city_index[0]
except IndexError:
    print("Город не найден")
    exit()

city_id = cities[index_in_list].get("id")
url_сelsius="http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a"

data = urllib.parse.urlsplit(url_сelsius)
query_data= urllib.parse.parse_qs(data.query)
query_data["id"][0]=city_id
query_data["appid"][0] = appid
new_query=urllib.parse.urlencode(query_data, doseq=True)

new_url_сelsius =  urllib.parse.urlunsplit((data.scheme, data.netloc, data.path, new_query, data.fragment))
response = requests.get(new_url_сelsius)

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# del_table = "DROP TABLE weather"
# cursor.execute(del_table)
# conn.commit()
try:
    cursor.execute("""CREATE TABLE weather
                       (id_city INTEGER PRIMARY KEY,
                       city VARCHAR(255),
                       date DATE,
                       temperature integer,
                        id_weather integer)
                    """)
except sqlite3.OperationalError:
    pass

try:
    add_city = [(f'{cities[index_in_list].get("id")}',
                f'{cities[index_in_list].get("name")}',
                 '{date}'.format(date=datetime.now().strftime('%Y.%m.%d')),
                 f'{response.json().get("main").get("temp")}',
                 f'{response.json().get("weather")[0].get("id")}')]
    cursor.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", add_city)
    conn.commit()
except sqlite3.IntegrityError:
    print("В базе данных уже есть следующая информация о погоде в выбранном Вами городе:")
    find_city = "SELECT * FROM weather WHERE id_city=?"
    cursor.execute(find_city, [(f'{cities[index_in_list].get("id")}')])
    print(cursor.fetchone())
    update_permission=input("Обновить  данные о погоде в этом городе? (Y / N/ Exit): ").lower()
    if update_permission !="y" and update_permission !="n" and update_permission !="exit":
        while True:
          update_permission = input("Неверный ввод. Обновить  данные о погоде в этом городе?  (Y / N): ").lower()
          if update_permission =="y" or update_permission =="n" or update_permission =="exit":
              break
    if update_permission=="y":
        del_city = "DELETE FROM weather WHERE id_city ='{data}'".format(data=cities[index_in_list].get("id"))
        cursor.execute(del_city)
        add_city = [(f'{cities[index_in_list].get("id")}',
                    f'{cities[index_in_list].get("name")}',
                     '{date}'.format(date=datetime.now().strftime('%Y.%m.%d')),
                     f'{response.json().get("main").get("temp")}',
                     f'{response.json().get("weather")[0].get("id")}')]
        cursor.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", add_city)
        conn.commit()
        print("Данные о погоде в выбранном Вами городе обноылены:")
    elif update_permission == "n" or update_permission == "exit":
        print("Данные о погоде в выбранном Вами городе остались без изменений:")

for row in cursor.execute("SELECT rowid, * FROM weather ORDER BY id_city "):
    print(row)

conn.close()