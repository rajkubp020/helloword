import numpy as np
import pandas as pd
data = np.genfromtxt('al10.dat',skip_header=19,max_rows=3601)

len(data)
# change Na
mask = data[:,1]==4
data[mask,1] = 9

sum(mask)
# change O2
mask = data[:,1] == 5
data[mask,1] = 4

sum(mask)
mask = data[:,1]==3
print(sum(mask))

b_pos = data[mask,:]

b_pos1 = b_pos.copy()
b_pos2 = b_pos.copy()

b_pos1[:,3:6] += 0.5
b_pos2[:,3:6] -= 0.5

len(b_pos1)

# change Na
mask = data[:,1]==9
data[mask,1] = 3

len(data)

data = np.vstack([data,b_pos1,b_pos2])
len(data)
data[:,0] = range(1,len(data)+1)


np.savetxt('./1.data',data,fmt=['%.0f']*2+['%.8f']*4+['%.0f']*3)

f = open('al10.dat','r')
g = open('1.dat','w')

counter = 0
mass = ['1 28.085', '2 26.982', '3 1.008', '4 15.999','','Atoms # charge','']
for ind,line in enumerate(f):
    if ind==2:
        g.write('{} atoms\n'.format(len(data)))
    elif ind==3:
        g.write('4 atom types\n')
    elif ind<11:
        g.write(line)
    else:
        break
f.close()

for i in mass:
    g.write(i+'\n')
    

f = open('1.data','r')

for ind,line in enumerate(f):
    g.write(line)

g.close()
