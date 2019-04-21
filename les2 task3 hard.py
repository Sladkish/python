
__author__ = 'Михайловский Василий Владимирович'

room_number = int(input("введите номер комнаты N, 1 ≤ N ≤ 2 000 000 000: "))
rooms=[]
block=1
blocks=[]
level=[]
max_room=[]
room_number1=room_number
while room_number1 > 0:
    room_number1=room_number1-block**2
    level.append(block)
    # blocks.append(block)
    rooms.append(block**2)
    max_room.append(sum(rooms))
    block=block+1

block=block-1
min_level=sum(level[:-1])
max_level=sum(level)
start_room=max_room[block-2]+1
end_room=start_room+rooms[-1]-1
print(f"комната расположена в блоке {block}на{block}")
# print(f"комната расположена между {min_level} и {max_level} этажами включительно")
# print(f"всего блоков в башне {blocks}")
# print(f"всего комнат в блоках {rooms}")
# print(f"максимальный номер комнаты в блоке {max_room}")
# print(f"комната расположена между {start_room} и {end_room} номерами")

for i in list(range(1,block+1)):
    room_level = list(range(start_room,start_room+block))
    start_room=start_room+block
    if (room_number in room_level):
        for j in list(range(block)):
            if room_level[j]==room_number:
                break
        break

room_level_number=min_level+i
print(f"Итак ответ - номер этажа: {room_level_number}, порядковый номер на этаже слева: {j+1}")

