__author__ = 'Михайловский Василий Владимирович'
class Triangle:

    def __init__(self, color, coordA ,coordB , coordC):
        self.color = color
        self.coordA = coordA
        self.coordB = coordB
        self.coordC = coordC
        self.AB=((self.coordB[0]-self.coordA[0])**2+(self.coordB[1]-self.coordA[1])**2)**0.5
        self.AC=((self.coordC[0]-self.coordA[0])**2+(self.coordC[1]-self.coordA[1])**2)**0.5
        self.BC=((self.coordC[0]-self.coordB[0])**2+(self.coordC[1]-self.coordB[1])**2)**0.5
    def perimeter(self):
        self.P=round(self.AB + self.AC + self.BC, 2 )
        return self.P
    def height(self):
        self.p=(self.AB + self.AC + self.BC)/2
        self.H=round(2*((self.p*(self.p-self.BC)*(self.p-self.AC)*(self.p-self.AB))**0.5)/self.BC, 2 )
        return self.H
    def area(self):
        self.S=round(self.BC*self.H/2, 2)
        return self.S
        

triang1=Triangle("blue", (0,0), (4,2), (55,23))
print(f"цвет заданного треугольника {triang1.color}")
print(f'периметр заданного треугольника {triang1.perimeter()}')
print(f'высота, опущенная на сторону a, заданного треугольника {triang1.height()}')
print(f'площадь заданного треугольника {triang1.area()}')







