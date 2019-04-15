#conding: utf-8

import os
import sys
import psutil

print("моя первая прога")
print("привет красавчик!")

name = input("Ваше имя: ")
print(name, ", добро пожаловать!")
answer = ''

   
answer=input(" Давай работать? (Y/N) ")

if answer =='Y':
   print("отлично хозяин")
   print("я умею")
   print( "[1] - выведу список файлов ")
   print( "[2] - выведу информацию о системе")
   print( "[3] - выведу список процессов")
   print( "[4] - продублирую файлы в текущей директории")
      do=int(input(" укажите номер действия  "))

   if   do == 1:
   	    print (os.listdir())
   elif do == 2:
   	    print( "Вот что я знаю о системе:")
   	    print( "Количество процессов: ", psutil.cpu_count())
   	    print( "Платформа: ", sys.platform)
   	    print( "Кодировка файловой системы ", sys.getfilesystemencoding())
   	    print( "текущая директория: ", os.getcwd())
   	    print( "текущий пользователь ", os.getlogin())
   elif do == 3:
   	    print (psutil.pids())
   else:
        pass
elif answer == 'N':
    print ("Goodbye")
else:
	print ("wtf?")