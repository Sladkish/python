

__author__ = 'Михайловский Василий Владимирович'


x=int(input("enter x "))
y=int(input("enter y "))
if x==y:
    print("Введены два одинаковых числа")
else:
    y=y+x
    x=y-x
    y=y-x
    print ("переменная x стала ",x)
    print ("переменная y стала ",y)

#   ВАРИАНТ С ПРОМЕЖУТОЧНОЙ ПЕРЕМЕННОЙ

# number1 = int(input("введите произвольное число  "))
# number2 = int(input("введите произвольное число  "))
# print( ' введено число номер 1' , number1 )
# print( ' введено число номер 2' , number2 )
# print( 'меняю местами' )
#
# temp_number=number1
#
# number1 = number2
# number2 = temp_number
# print( 'число номер 1' , number1 )
# print( 'число номер 2' , number2 )

