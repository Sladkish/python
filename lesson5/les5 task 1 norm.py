
__author__ = 'Михайловский Василий Владимирович'
import sys
import easy
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("ping - тестовый ключ")
    print("1. Перейти в папку <dir_name> ")
    print("2. Посмотреть содержимое текущей папки")
    print("3. Удалить папку <dir_name> ")
    print("4. Cоздать папку <dir_name> ")

def ping():
    print("pong")


do = {
    "help": print_help,
    "ping": ping,
    "1": easy.ch_dir,
    "2": easy.lst_dir,
    "3": easy.remove_dir,
    "4": easy.make_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        if key=="4" or key=="3" or key=="1":
            do[key](dir_name)
        else:
            do[key]()

    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")




