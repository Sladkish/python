__author__ = 'Михайловский Василий Владимирович'

import os
def lst_dir():
    print(os.listdir(os.getcwd()))


def remove_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError :
        print('директория {} не существует'.format(dir_name))



def ch_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(fr"{dir_name}")
        print("перешел в: ", os.getcwd())
    except FileNotFoundError :
        print('директория {} не существует'.format(dir_name))


def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))



