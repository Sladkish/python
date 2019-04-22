# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.


__author__ = 'Михайловский Василий Владимирович'


equation =input("введите уравнение прямой вида y = kx + b: ")

x=float(input("введите значение координату х: "))
k=float(equation[equation.index("=")+1:equation.index("x")])
b=float(equation[equation.index("x")+3:])
sign=equation[equation.index("x")+2:equation.index("x")+3]
if sign == "-":
    b=-1*b
print(sign)
print(k)
print(b)
y=k*x+b
print(y)
