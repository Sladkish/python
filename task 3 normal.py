__author__ = 'Михайловский Василий Владимирович'
a= int(input("Введите коэфициэнт уравнения a: "))
b= int(input("Ведите коэфициэнт уравнения b: "))
c= int(input("Ведите коэфициэнт уравнения c: "))

D=b*b-4*a*c
if D<0:
    print("вещественнх корней нет")
elif D==0:
    x=(-1*b)/(2*a)
    print ("уравнение имеет один корень" , x)
else:
    x1=((-1*b)-D**0.5)/(2*a)
    x2=((-1*b)+D**0.5)/(2*a)
    print ("первый корень уравнения равен " , x1)
    print ("второй корень уравнения равен" , x2)