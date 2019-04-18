__author__ = 'Михайловский Василий Владимирович'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#expr="465/50 + -51 15/25"
expr=input("введите выражение: ")    
expr_part= expr.split(" ")
fractions=[]
for i in expr_part:
    if "/" in i:
        expr_part.remove(i)
        fractions.append(i.split("/"))
       
x=int((fractions[0][0]))
y=int((fractions[0][1]))
x1=int((fractions[1][0]))
y1=int((fractions[1][1]))
if y==0 or y1==0:
    print("ошибка, деление на ноль. знаменатель не может быть равен нулю")
else:
    if len(expr_part)==3:
        if "+" in expr_part:
            sign="+"
            expr_part.remove("+")
        elif "-" in expr_part:
            sign="-"
            expr_part.remove("-")
            n=int(expr_part[0])
            n1=int(expr_part[1])
        
    elif len(expr_part)==2:
            if "+" in expr_part:
                sign="+"
                if expr_part.index("+")==1:
                    n=int(expr_part[0])
                    n1=0
                else:
                    n=0
                    n1=int(expr_part[1])
            elif "-" in expr_part:
                sign="-"
                if expr_part.index("-")==1:
                    n=int(expr_part[0])
                    n1=0
                else:
                    n=0
                    n1=int(expr_part[1])
    elif len(expr_part)==1:
            if "+" in expr_part:
                sign="+"
                
            elif "-" in expr_part:
                sign="-"
            else:
                print("ошибка")  
            n=0
            n1=0
    if sign=="+":
        X=y1*(n*y+x)+y*(n1*y1+x1)
        
    if sign=="-":    
        X=y1*(n*y+x)-y*(n1*y1+x1)
    Y=y*y1
    N=X//Y
    X=X%Y
    d=gcd(X,Y)

    if N==0 and X==0:
        print("Результат выражения: 0 " )
    elif N==0:
        print(f"Результат выражения: {int(X/d)}/{int(Y/d)}")
    elif X==0:
        print("Результат выражения: ", N)
    else:
        print(f"Результат выражения: {N} {int(X/d)}/{int(Y/d)}")