__author__ = 'Михайловский Василий Владимирович'
import os

path = os.path.join("data", "fruits.txt")
f=open(path,"r", encoding = "UTF-8")
list1=f.read().split("\n")
f.close()
print(list1)

# ПОЧЕМУТО уменя первое слово в списке имеет вид \ufeffАбрикос. следующими строчками я удалял приставку \ufeff
# first_word=list1[0]
# print(first_word)
# list1.remove(first_word)
# swap=first_word.split('\ufeff')
# list1.append(swap[1])
# print(list1)

list2=list(map(chr, range(ord('А'), ord ('Я')+1)))

for word in list1:
    for letter in list2:
         if word[0]==letter:
            path = os.path.join("data", f"fruit_{letter}.txt")
            my_file = open(path,"w")
            my_file.close()
for word in list1:
    for letter in list2:
         if word[0]==letter:
            path = os.path.join("data", f"fruit_{letter}.txt")
            my_file = open(path,"a")
            my_file.write(f"{word}\n")
            my_file.close()
            

