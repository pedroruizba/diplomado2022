
##===========PARA CALCULAR VALOR DE X
p1=(-4,-2)
p2=(1,5)
y=3.7

#-4+ (3.7 - -2) · (1--4) / (5 - -2) = 0.071429
def fn(y,p1,p2):
    a=(y-p1[1])*(p2[0]-p1[0])
    b=(p2[1]-p1[1])
    return p1[0]+(a/b)

print("Cuando Y=",y," X=",fn(y,p1,p2))