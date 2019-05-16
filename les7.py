__author__ = 'Михайловский Василий Владимирович'
import random
count=4
def create_loto_lst(count,lst):
    j = 0
    while j < count:
        change_value = random.choice(lst)
        for n, el in enumerate(lst):
            if el == change_value and el != "":
                lst[n] = ""
                j += 1
    return lst

def create_loto_matrix():
    lst = set()
    while len(lst)<27:
        lst.add(random.randint(1,90))
    lst=list(lst)
    random.shuffle(lst)
    lst1=create_loto_lst(count,sorted(lst[:9]))
    lst2=create_loto_lst(count,sorted(lst[9:18]))
    lst3=create_loto_lst(count,sorted(lst[18:27]))
    matrix=[lst1,
            lst2,
            lst3]
    return matrix

def check_ticket(value,matrix):
    result = None
    for line_number, line in enumerate(matrix):
        for index, el in enumerate(line):
            if el == value:
                result=[line_number,index]
    return result

def find_winner(matrix):
    result = 1
    for line_number, line in enumerate(matrix):
        for index, el in enumerate(line):
            if type(el) == int:
                result=None
                break
    return result

def my_gen():
    lst=[i for i in range(1,91)]
    random.shuffle(lst)
    for index, item in enumerate(lst):
        yield item, len(lst)-index-1

def pMatrix(matrix):
    for row in matrix:
        print(*list(map('{{:>{length}}}'.format(length=3).format, row)))


player_ticket=create_loto_matrix()
comp_ticket=create_loto_matrix()

print("Да начнется игра!")

for barrel in my_gen():
    print(f"новый бочонок {barrel[0]}, (осталось {barrel[1]} )")
    print("------------Ваша карточка-----------")
    pMatrix(player_ticket)
    print("---------Карточка компьютера--------")
    pMatrix(comp_ticket)

    comp_check = check_ticket(barrel[0], comp_ticket)
    if comp_check is not None:
        comp_ticket[comp_check[0]][comp_check[1]] = "-"
    player_check=check_ticket(barrel[0], player_ticket)

    answer = input("Зачеркнуть цифру? (Y / N): ").lower()


    if answer !="y" and answer !="n" :
        while True:
          answer = input("Неверный ввод. Зачеркнуть цифру? (Y / N): ").lower() 
          if answer=="y" or answer=="n" :
              break    
 
    if answer=="y" and player_check is not None:
        player_ticket[player_check[0]][player_check[1]] = "-"
    elif answer == "y" and player_check is None:
        print("Ты проиграл, на твоей карточке нет такой цифры. Лох!")
        break
    elif answer == "n" and player_check is not None:
        print(f"Ты проиграл, нужно было зачеркнуть из карточки эту цифру. Лох!")
        print(f"Адрес цифры: строка - {player_check[0]+1},номер в строке - {player_check[1]+1}.")
        break
    elif answer == "n" and player_check is None:
        pass
 

    if find_winner(comp_ticket) == 1 and find_winner(player_ticket) == 1 :
        print("Ничья")
        break
    if find_winner(comp_ticket)==1:
        print("Конец игры, компьютер зачеркивает последний боченок и побеждает")
        print("Ты неудачник!")
        pMatrix(comp_ticket)
        break
    if find_winner(player_ticket)==1:
        print("Конец игры, игрок зачеркивает последний боченок и побеждает")
        print("Ваще красава, мужик!")
        pMatrix(player_ticket)
        break
print("Конец игры!")







