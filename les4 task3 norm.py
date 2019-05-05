
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
#

__author__ = 'Михайловский Василий Владимирович'
import os
import random
import re

n=2500
path = os.path.join("data", "numbers.txt")
with open(path,"w", encoding = "UTF-8") as f:
     for el in range(n):
         num=random.randint(0, 9)
         f.write("%s" % num)
     f.close()
f=open(path,"r", encoding = "UTF-8")
lst=f.readlines()
f.close()
print(lst[0])
print(type(lst[0]))
ln=0
numbers = re.findall(r'[0]{1,}|[1]{1,}|[2]{1,}|[3]{1,}|[4]{1,}|[5]{1,}|[6]{1,}|[7]{1,}|[8]{1,}|[8]{1,}', lst[0])
print(numbers)
for i in numbers:
    if len(i)>ln:
        ln=len(i)
        super_num=i
print(ln)
print(super_num)