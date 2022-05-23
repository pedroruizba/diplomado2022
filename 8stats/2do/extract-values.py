#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
#

import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')


print('head',iris.head())
print('')


# 
# ========Metadata tupla=========
#             ALL DATA
'''
data = []
for i in iris.index:
    data.append(tuple(iris.values[i]))
allnodes = tuple(data)
print(allnodes)
'''
#        ONE COLUMN


print('======== SEPAL LENGTH (TUPlA) ========')
#print(irisTUP["sepal length"])
irisTUP = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal length'])
dataTUP = []
for i in irisTUP.index:
    dataTUP.append(tuple(irisTUP.values[i]))
allnodes = tuple(dataTUP)
print(allnodes)



print('======== SEPAL WIDTH (dictionary) ========')
dict_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal width']).to_dict()
print(dict_from_csv)



print('======== SEPAL LENGTH (list) ========')
list_from_csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',names = ['sl','sw','pl','pw','class'])
datalist = list_from_csv.pl.to_list()
print(datalist)

