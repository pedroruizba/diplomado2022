#
# read binary file (dictionary)
# and print it
#

import pickle
import pprint #impresion legible de cadena u objeto


with open('dic.bin','rb') as fh:
        adic = pickle.load(fh) 

print(type(adic))
print("Sin pprint:\n",adic)
print("Con pprint:\n")

pprint.pprint(adic)
