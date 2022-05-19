import random
lst=['aguila','sello']

aguila=0
sello=0
cantidad_veces=10

for n in range(cantidad_veces):
    tiro=random.choice(lst)
    if tiro == 'aguila':
        aguila+=1
    else:
        sello+=1

print("Total Aguila: ", aguila)
print("Total Sello: ", sello)
