# write a program to remove the duplicate from strings

from sys import argv
args=argv[1]
l=''
for i in args:
    if i not in l:
        l=l+i
print(l)

#######################################################################

'''s=input('enter the strings:')
s1=''
for i in s:
    if i not in s1:
        s1=s1 + i
print(s1)'''