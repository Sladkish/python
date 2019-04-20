__author__ = 'Михайловский Василий Владимирович'
num = int(input("введите произвольное целое число "))
i=10
big_digit = 0
if num==0:
    print("введен 0")
else:
    print("Число", num, "состоит из следующих  цифр: ")
    if num < 0:
        num=num*-1

    while num > 0:
      digit = int(num % i)
      num=(num-digit)/i
      print(digit)
      if digit>big_digit:
          big_digit=digit

    print("наибольшая цифра: ", big_digit)
