__author__ = 'Михайловский Василий Владимирович'

import sqlite3
import json
import os
import sys

print('sys.argv = ', sys.argv)

def print_help():
    print("1.help-получение справки\
           \n2.exp-экспорт данных в json-фаил")


def export_data():
    choose_city = input("введите город, данные о погоде которого необходимо экспортировать из базы данных в json-фаил : ")
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    rows = db.execute("SELECT * from weather WHERE city='{}'".format(choose_city)).fetchall()

    conn.commit()
    conn.close()
    if len(rows) == 0:
        print(f"В базе данных нет информации по городу {choose_city}")
    else:

        with open(os.path.join("data", 'filename.json'), 'w', encoding='UTF-8') as f:
            json.dump([dict(ix) for ix in rows], f)
            print(f"экспортированны следующие данные {[dict(ix) for ix in rows]}")

        # with open(os.path.join("data", 'filename.json'), 'r', encoding='UTF-8') as f:
        #     d = json.load(f)
        #     print(d)


do = {"help": print_help, "exp": export_data}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")






