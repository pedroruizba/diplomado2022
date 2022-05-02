
#Calculadora: https://www.calculatoratoz.com/es/radio-del-circulo-inscrito-calculadora/node-180?FormulaId=172

import math


print("\n\n Radio de un circulo inscrito en un triángulo de lados a, b, y c.  \n")

a=float(input("Inserte valor de a: "))
b=float(input("Inserte valor de b: "))
c=float(input("Inserte valor de c: "))

suma=a+b

if (c < suma):
    s=0.5*(a+b+c)
    r=math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    r_rounded = round(r, 2)
    s_rounded = round(s, 2)
    print("S=")
    print(s_rounded)
    print("R=")
    print(r_rounded)
else:
    print("El valor de c no puede ser mayor a la suma de a y b")