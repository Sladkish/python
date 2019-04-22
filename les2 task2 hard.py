__author__ = 'Михайловский Василий Владимирович'

date=input("Ведите дату ввиде dd.mm.yyyy: ")
date1=date
point_ind=[]
for i in date1:
    if i==".":
        # print("индекс точки ",date1.index("."))
        point_ind.append(date1.index("."))
        date1=date1[0:date1.index(".")]+"/"+date1[date1.index(".")+1:]
        # print(date1)
        # print(point_ind)

day = date[:point_ind[0]]
print("введен день: ", day)
month = date[point_ind[0]+1:point_ind[1]]
print("введен месяц: ", month)
year = date[point_ind[1]+1:]
print("введен год: ", year )
if int(month)>12 or int(month)<=0:
    print("некорректная дата, неверно указан месяц")

elif int(year)>9999 or int(year)<=0:
    print("некорректная дата, неверно указан год")

elif int(day)>31 or int(day)<=0:
    print("некорректная дата, неверно указан день")

elif int(day)==31 and (int(month)==4 or 6 or 9 or 11 or 2):
    print("некорректная дата, неверно указан день")

elif len(day)<=1 or len(month)<=1:
    print("некорректная дата, день или месяц введены не по образцу")
else:
    print("введена коректная дата", date)

