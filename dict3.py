# write a program to find the number of occurence of each letter given in a string.

s=input('enter the sentence:')
d={}

for i in s:
    d[i]=d.get(i,0) +1
    print(d)
print(d)

'''for j,k in d.items():
    print('{}={} times'.format(j,k))'''


