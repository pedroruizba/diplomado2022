#
# 2do
#
import pickle

d={'20135555':'Roberto Bolaños', '20221010':'Paulina Rubio', '20218888':'Will Smith'}

with open('dic.bin','wb') as fh:
        pickle.dump(d,fh)

print('done...')

