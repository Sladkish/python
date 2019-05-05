__author__ = 'Михайловский Василий Владимирович'



import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp < file_name > - создает копию указанного файла")
    print("rm < file_name > - удалить указанный файл")
    print("cd <full_path or relative_path> - поменять текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))

def copy_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.exists(os.path.join(os.getcwd(), "copy_"+name)):
        print("копия данного файла уже сушествует")
        return
    try:
        shutil.copyfile(os.path.join(os.getcwd(), name), os.path.join(os.getcwd(), "copy_"+name))
        print(f'фаил {name} скопирован в фаил copy_{name}')
    except FileNotFoundError :
        print('фаил {} не существует'.format(name))


def remove_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    resolution = input(f"вы точно хотите удалить фаил {name}, Y or N :")
    if resolution=="Y":
        try:
            os.remove(os.path.join(os.getcwd(), name))
            print(f'фаил {name} удален')
        except FileNotFoundError:
            print('фаил {} не существует'.format(name))
    elif resolution == "N":
        print('отмена команды удаления')
    else:
        print('неверная команда')



def ch_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(name)

        print("перешел в: ", os.getcwd())
        new_path=os.getcwd()
        print(new_path)
    except FileNotFoundError :
        print('директория {} не существует'.format(name))


def full_path():
    if not name:
        print("Необходимо указать имя директории или файла вторым параметром")
        return
    try:
        print("полный путь: ", os.path.abspath(name))
    except FileNotFoundError :
        print('директория {} не существует'.format(name))



def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": ch_dir,
    "ls": full_path

}





try:
    name = sys.argv[2]
except IndexError:
    name = None

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