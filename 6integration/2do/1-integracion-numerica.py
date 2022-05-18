
from math import sin, sqrt

def f(x):
    return 2*(sin(sqrt(x)))-x

a = 0
b = 1.9724
m = (a+b)/2

r1 = f(a)*(b-a)
print("Regla del Rectángulo: ",r1)

r2 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print("Regla de Simpson: ",r2)
