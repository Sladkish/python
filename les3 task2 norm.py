
__author__ = 'Михайловский Василий Владимирович'


def sort_to_max(arr):
    for n in list(range(0,len(arr)-1)):
        min=arr[n]
        for i in list(range(n+1,len(arr))):
            # print(i)
            if arr[i]<min:
                min=arr[i]
                swap=arr[n]
                arr[n]=min
                arr[i]=swap
    return arr

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# ВТОРОЙ ВРИАНТ
# def sort_to_max(arr):
#     arr1=[]
#     for j in list(range(len(arr))):
#         arr1.append(min(arr))
#         arr.remove(min(arr))
#     return arr1
#
# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
