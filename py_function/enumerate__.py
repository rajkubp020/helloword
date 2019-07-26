# L = ['apples', 'bananas', 'oranges']
# for idx, val in enumerate(L):
#   print("index is %d and value is %s" % (idx, val))
import pandas as pd
import numpy as np

data = np.genfromtxt("al10.dat",skip_header=18,max_rows=3601)

# print('zsddfcg',len(data))
for index, value in enumerate(data[:,:]):
     id=value[0]
     atom=value[1]
     print('index={}  id={}  value={}' .format(index,id, atom))
     # print( '{} atoms\n'.format(len(data)))
     # print('{} atoms\n'.format(len(data)))

# Principal Index Fund - MidcapPrincipal PNB AMC Private Ltd.
# MOSt Shares M100Motilal Oswal AMC Ltd.
list(enumerate(['a', 'b', 'c']))
