
__author__ = 'Михайловский Василий Владимирович'

k=[1 ,2, 3, 4, 4, 5, 6,7,8,4,9,0]


def my_filter(condition,args):
    arr1=[]
    for i in args:
         if condition(i)==True:
             arr1.append(i)
    return iter(arr1)

a=list(my_filter(lambda x: x==4,k))
print(a)
#         