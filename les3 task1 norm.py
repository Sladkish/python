__author__ = 'Михайловский Василий Владимирович'

def fibonachi(n,m):
    if n==m:
        F=[]
    elif n>m:
        F=None
    else:
        F=[1,1]
        for i in list(range(m-2)):
            F.append(F[i]+F[i+1])
        for j in list(range(n-1)):
            F.remove(F[0])
    return F    

print(fibonachi(2,20))

#F=[1,1]
#for i in list(range(m-3)):
#    F.append(F[i]+F[i+1])
#print(F)   
#for j in list(range(n-2)):
#    F.remove(F[0])
#print(F)
    
