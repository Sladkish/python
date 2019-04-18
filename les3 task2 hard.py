__author__ = 'Михайловский Василий Владимирович'
import os


def salary(hours_worked,standart_hours, stadart_money):
    money=[]
    for item in hours_worked:
        if item > 40:
            money.append(standart_hours*stadart_money/standart_hours+(item-standart_hours)*2*stadart_money/standart_hours)
        else:
            money.append(item*stadart_money/standart_hours)
    return money

standart_hours=40
standart_money=10000

path = os.path.join("data", "hours_of.txt")
f=open(path,"r", encoding = "UTF-8")
list=f.readlines()
print(list)
f.close()
wokers_hours=[]
wokers_hours2=[]
i=0
for item in list:
    wokers_hours.append((list[i].split(" "))[0])
    wokers_hours2.append(wokers_hours[i].split("-"))
    i+=1

hours=[]
wokers_name=[]
j=0
for item in wokers_hours2:
    hours.append(int((wokers_hours2[j][1])))
    wokers_name.append((wokers_hours2[j][0]))

    j+=1
print(f"Часы отработанные рабочими в неделю: {hours}")
print(f"Фамилии рабочих, работавших на этой недели {wokers_name}")

money=salary(hours,standart_hours, standart_money)
print((f"Дениги заработанные рабочими за неделю: {money}"))
n=0
wokers_money=[]
for name in wokers_name:
    wokers_money.append(name+" earned this week "+str(money[n])+ " rubles" )
    n+=1
print(wokers_money)
path = os.path.join("data", "money.txt")
with open(path,"w", encoding = "UTF-8") as f:
    for item in wokers_money:
        f.write("%s\n" % item)