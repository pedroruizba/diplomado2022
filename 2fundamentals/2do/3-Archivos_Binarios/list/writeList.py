#
# binary files
#

import pickle

aList = ["iphone", "xioami", ["telefono 1", "telefono 2"], "opo"]

with open('list.bin','wb') as fh:
        pickle.dump(aList,fh)

print('done...')
