#Crear funcion 1 al 10 con incrementos de .1
# generar una función para producir puntos
# para ser usado como eje x
#
# APORTE
# -> un punto inicial
# -> b punto final
# -> c incremento
#
# PRODUCCIÓN
# <- lista de puntos
#
# por ejemplo para este rango [1,10,.1]
# producirá 100 puntos
# [1.0, 1.1, ... , 9.9, 10]

from decimal import Decimal

def serie(start,fin,incremento):
    c=start
    while c<=fin+incremento:
        print ("{0:.1f}".format(c))
        c+=incremento

start=int(1)
fin=int(10)
incremento=Decimal(0.1)
serie(start,fin,incremento)
