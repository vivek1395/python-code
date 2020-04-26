# write a program to find the vowels from a given sentence.

s='my name is vivek kumar'
v=['a','e','i','o','u']
f=[]
s=list(s)
for i in s:
    if i in v:
        if i not in f:
            f.append(i)
print('vowels present in s are:',f)

