'''#===========PARA CALCULAR VALOR DE Y
p1=(3,7.2)
p3=(7,-4.4)
x=4.3

def fn(x,p1,p3):
    a=(p3[1]-p1[1])/(p3[0]-p1[0])
    b=x-p1[0]
    return a*b+p1[1]

print("Cuando X=",x," Y=",fn(x,p1,p3))
'''


 #=====PARA CALCULAR Polinomio interpolante de Lagrange
p1=(-2,4)
p2=(-1,-2)
p3=(3,5)
p4=(4.3,11)
x=7.7

def fn(x,p1,p2,p3,p4):
    a=((x-p2[0])/(p1[0]-p2[0]))
    b=((x-p3[0])/(p1[0]-p3[0]))
    c=((x-p4[0])/(p1[0]-p4[0]))
    d=a*b*c*p1[1]

    a1=((x-p1[0])/(p2[0]-p1[0]))
    b1=((x-p3[0])/(p2[0]-p3[0]))
    c1=((x-p4[0])/(p2[0]-p4[0]))
    d1=a1*b1*c1*p2[1]

    a2=((x-p1[0])/(p3[0]-p1[0]))
    b2=((x-p2[0])/(p3[0]-p2[0]))
    c2=((x-p4[0])/(p3[0]-p4[0]))
    d2=a2*b2*c2*p3[1]

    a3=((x-p1[0])/(p4[0]-p1[0]))
    b3=((x-p2[0])/(p4[0]-p2[0]))
    c3=((x-p3[0])/(p4[0]-p3[0]))
    d3=a3*b3*c3*p4[1]
      
    return d+d1+d2+d3

print("Cuando x=",x," y=",fn(x,p1,p2,p3,p4))




