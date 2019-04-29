__author__ = 'Михайловский Василий Владимирович'
import copy

def check_matrix(matrix): 
    answer="NO"
    for line in matrix:
        if sum(line)>=2:
            answer="YES"          
    return answer  

def pMatrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()

#Координаты ферзей
coordinate1=[3,1]
coordinate2=[5,2]
coordinate3=[2,3]
coordinate4=[8,4]
coordinate5=[1,5]
coordinate6=[7,6]
coordinate7=[4,7]
coordinate8=[6,8]


n=8
m=8
matrix = []
for i in range(n):
    matrix.append([0] * m)
print("Нулевая матрица")
pMatrix(matrix)

matrix[coordinate1[0]-1][coordinate1[1]-1]=1
matrix[coordinate2[0]-1][coordinate2[1]-1]=1
matrix[coordinate3[0]-1][coordinate3[1]-1]=1
matrix[coordinate4[0]-1][coordinate4[1]-1]=1
matrix[coordinate5[0]-1][coordinate5[1]-1]=1
matrix[coordinate6[0]-1][coordinate6[1]-1]=1
matrix[coordinate7[0]-1][coordinate7[1]-1]=1
matrix[coordinate8[0]-1][coordinate8[1]-1]=1

print("Матрица с ферзями")
pMatrix(matrix)

rotate_matrix=list(map( list, zip(*matrix)))

print("Транспонированная матрицы с ферзями")
pMatrix(rotate_matrix)

diagonal_matrix_left=copy.deepcopy(matrix)
diagonal_matrix_right=copy.deepcopy(matrix)

for i, line in enumerate(diagonal_matrix_right):
    for _ in range(i):
        line.insert(0,0)
    for _ in range(m-i-1):
        line.append(0)  
        
print("Матрица диагоналей №1")
pMatrix(diagonal_matrix_right)

rotate_diagonal_matrix_right=list(map( list, zip(*diagonal_matrix_right)))
print("транспонированная матрица диагоналей №1")
pMatrix(rotate_diagonal_matrix_right)

for i, line in enumerate(diagonal_matrix_left):
    for _ in range(i):
        line.append(0) 
    for _ in range(m-i-1):
        line.insert(0,0)         
print("Матрица диагоналей №2")
pMatrix(diagonal_matrix_left)


rotate_diagonal_matrix_left=list(map( list, zip(*diagonal_matrix_left)))
print("Tранспонированная матрица диагоналей №2")
pMatrix(rotate_diagonal_matrix_left)


print("Пересечения по горизонтали: ", check_matrix(matrix))
print("Пересечения по вертикали: ", check_matrix(rotate_matrix))
print("Пересечения по диагонали: ", check_matrix(rotate_diagonal_matrix_right))
print("Пересечения по диагонали: ", check_matrix(rotate_diagonal_matrix_left))


  




