#
# 2do
#
import pickle

t=("enero","febrero","marzo","abril","mayo")

with open('tuple.bin','wb') as fh:
        pickle.dump(t,fh)

print('done...')