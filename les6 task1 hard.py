__author__ = 'Михайловский Василий Владимирович'
import os
import re

class Worker:
    def __init__(self, name, surname, salary, position, hours_rate, hours_actual):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.position = position
        self.hours_rate = hours_rate
        self.hours_actual = hours_actual
    
    def find_salary(self):
        if self.hours_actual >self.hours_rate:
            self.money=(self.salary + (self.hours_actual-self.hours_rate)*2*self.salary/ self.hours_rate)
        else:
            self.money=(self.hours_actual*self.salary/self.hours_rate)
        return round(self.money,2)
    
        
path = os.path.join("data", "wokers.txt")
f=open(path,"r", encoding = "UTF-8")
wokers_from_file=f.read().split("\n")
f.close()
path = os.path.join("data", "hours_of.txt")
f=open(path,"r", encoding = "UTF-8")
hours_from_file=f.read().split("\n")
f.close()

hours=[]
workers=[]
for el in wokers_from_file[1:]:
    el=re.sub(" +", " ", el)
    el=el.split(" ")
    workers.append(el)
print(workers)

for unit in hours_from_file[1:]:
     unit=re.sub(" +", " ", unit).split(" ")
     hours.append(unit)
print(hours)

lst_Workers=[]

for el_w, line_w  in enumerate(workers):
    print(el_w, line_w)
    for el_h, line_h in enumerate(hours):
        if line_h[1]==line_w[1]:
            workers[el_w].append(line_h[2])
            lst_Workers.append(Worker(workers[el_w][0], workers[el_w][1],
            int(workers[el_w][2]), workers[el_w][3], int(workers[el_w][4]),
            int(workers[el_w][5])))

print(f"работник {lst_Workers[0].surname}, заработал {lst_Workers[0].find_salary()}")
print(f"работник {lst_Workers[4].surname}, заработал {lst_Workers[4].find_salary()}")
print(f"работник {lst_Workers[2].surname}, заработал {lst_Workers[2].find_salary()}")


