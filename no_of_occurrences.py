# write a program to find the number of character in a given string.

#input= 'vvviivveeekk'
#output= v-5, i=2, e=3, k=2

s=input('enter the strings:')
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x] + 1
    else:
        d[x]=1
for k,v in d.items():
    print('{}={} times'.format(k,v), end=',')





