l=[(i,j) for i in range(1,5) for j in range(i,2*i)]
print(l)

from math import sqrt

l=[(x,sqrt(x)) for x in range(1,10)]
for i,j in l:
    print('root value for {} is {:2.2f}'.format(i,j))
