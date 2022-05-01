from cmath import sin
import math


print("\n\n Evaluar las funciones y=sin(2x) para x=1.3\n En la función y=e^(1-2x) en x=-0.45 \n")

print("\n\nFunción y=sin(2x) para x=1.3")

y = sin(2*1.3)
print("Resultado 1:")
print(y)


print("\n\nFunción y=e^(1-2x) en x=-0.45 ")

y2 = math.exp(1-2*(-0.45))
print("Resultado 2:")
print(y2)
