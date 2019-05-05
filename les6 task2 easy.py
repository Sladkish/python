__author__ = 'Михайловский Василий Владимирович'
import sys

class Trapezium:

    def __init__(self, coordA ,coordB , coordC, coordD):
        self.coordA = coordA
        self.coordB = coordB
        self.coordC = coordC
        self.coordD = coordD
        self.AB=((self.coordB[0]-self.coordA[0])**2+(self.coordB[1]-self.coordA[1])**2)**0.5
        self.AD=((self.coordD[0]-self.coordA[0])**2+(self.coordD[1]-self.coordA[1])**2)**0.5
        self.BC=((self.coordC[0]-self.coordB[0])**2+(self.coordC[1]-self.coordB[1])**2)**0.5
        self.CD=((self.coordD[0]-self.coordC[0])**2+(self.coordD[1]-self.coordC[1])**2)**0.5
        self.AC=((self.coordC[0]-self.coordA[0])**2+(self.coordC[1]-self.coordA[1])**2)**0.5
        self.BD=((self.coordD[0]-self.coordB[0])**2+(self.coordD[1]-self.coordB[1])**2)**0.5
        self.d1=round(self.AC,2)
        self.d2=round(self.BD,2)
        #далее идет проверка свойств трапеции. ищутся паралельные стороны и проверяется свойство d1^2+d2^2=2*a*b+c^2+b^2
        try:
            self.k1=(self.coordB[1]-self.coordA[1])/(self.coordB[0]-self.coordA[0])
            self.b1=self.coordA[1]-self.k1*self.coordA[0]
        except ZeroDivisionError:
            self.k1 = None
            self.b1 = self.coordA[0]
        print(f"сторона AB лежит на прямой с коэффициентами: k1={self.k1}, b1={self.b1}")

        try:
            self.k2=(self.coordD[1]-self.coordC[1])/(self.coordD[0]-self.coordC[0])
            self.b2=self.coordC[1]-self.k2*coordC[0]
        except ZeroDivisionError:
            self.k2 = None
            self.b2 = self.coordC[0]
        print(f"сторона CD лежит на прямой с коэффициентами: k2={self.k2}, b2={self.b2}")

        try:
            self.k3=(self.coordC[1]-self.coordB[1])/(self.coordC[0]-self.coordB[0])
            self.b3=self.coordB[1]-self.k3*self.coordB[0]
        except ZeroDivisionError:
            self.k3 = None
            self.b3 = self.coordB[0]
        print(f"сторона BC лежит на прямой с коэффициентами: k3={self.k3}, b4={self.b3}")

        try:
            self.k4=(self.coordD[1]-self.coordA[1])/(self.coordD[0]-self.coordA[0])
            self.b4=self.coordA[1]-self.k4*self.coordA[0]
        except ZeroDivisionError:
            self.k4 = None
            self.b4 = self.coordA[0]
        print(f"сторона AD лежит на прямой с коэффициентами: k4={self.k4}, b4={self.b4}")

        if self.k1 == self.k2 and self.k3 != self.k4 and (round((self.AC ** 2 + self.BD ** 2),5) == \
                 round( (self.AD ** 2 + self.BC ** 2 + 2 * self.AB * self.CD),5)):
            print("это трапеция")
            self.c=round(self.AD,2)
            self.d=round(self.BC,2)
            if self.AB < self.CD:
                self.a= round(self.AB,2)
                self.b = round(self.CD,2)
            else:
                self.a = round(self.CD,2)
                self.b = round(self.AB,2)

        elif self.k3 == self.k4 and self.k1 != self.k2 and (round((self.AC ** 2 + self.BD ** 2),5) == \
                round((self.AB ** 2 + self.CD ** 2 + 2 * self.AD * self.BC),5)):
            print("это трапеция")
            self.c=round(self.AB,2)
            self.d=round(self.CD,2)
            if self.BC < self.AD:
                self.a = round(self.BC,2)
                self.b = round(self.AD,2)
            else:
                self.a = round(self.AD,2)
                self.b = round(self.BC,2)

        else:
            print("Это не трапеция. Введите другие кординаты.")
            sys.exit()

    def isosceles(self):
        if self.c==self.d:
            result = True
        else:
            result = False
        return result

    def perimeter(self):
        self.P=self.a + self.b + self.c+ self.d
        return self.P
    def area(self):
        self.S=round(((self.a+self.b)/2)*(self.c**2-(((self.b-self.a)**2+self.c**2-self.d**2)/(2*self.b-2*self.a))**2)**0.5, 3)
        return self.S

trap1=Trapezium((0,0), (2,4), (4,5), (6,3))

# print(f"сторона AB равна: {trap1.AB}")
# print(f"сторона BC равна: {trap1.BC}")
# print(f"сторона CD равна: {trap1.CD}")
# print(f"сторона AD равна: {trap1.AD}")
# print(f"диагональ AC равна: {trap1.AC}")
# print(f"диагональ BD равна: {trap1.BD}")

print(f"меньшее основание a равно:{trap1.a}")
print(f"большее основание b равно:{trap1.b}")
print(f"боковая сторона с равна:{trap1.c}")
print(f"боковая сторона d равна:{trap1.d}")
print(f"диагональ d1 равна:{trap1.d1}")
print(f"диагональ d2 равна:{trap1.d2}")


print(f'периметр заданной трапеции {trap1.perimeter()}')
print(f'площадь заданной трапеции {trap1.area()}')
print(f'является ли заданная трапеция ранобедренной? Ответ: {trap1.isosceles()}')








