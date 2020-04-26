'''list= [eval(input('enter the list:'))]
print(list)
print(list[0])'''

# list function

'''l=list(range(2,22,2))
print(l)

# string to list conversion

s="vivek kumar"
l=list(s)
print(s)
print(l)

#######################################################

s="vivek loves python"

l=s.split()  # split function split the string into list.

print(s)
print(l)
print(type(l)'''


a=[1,2,1]
b=[2,4]
a.append(b)
print(a) ## [1, 2, [2, 4]]  this is nested list
print('length of string is:',len(a))  # 4
print(a.count([2,4])) # output is 1. hence it did not count the nested list element.

print(a.index(2))

a.insert(2,'vivek')  # list.insert(index,element)
print(a)

a.insert(10,'kumar')   # we are inserting this element at index 10 even though max index is 4
# hence it will insert at index at 5 which is the next available index in the list.
print(a.index('kumar'))

c=[1,2]
d=[2,3,400,'vivek']
c.extend(d)  # [1, 2, 2, 3, 400,'vivek']
c.extend('kumar') # [1, 2, 2, 3, 400, 'vivek', 'k', 'u', 'm', 'a', 'r']
f=['Raj']
c.extend(f) # [1, 2, 2, 3, 400, 'vivek', 'k', 'u', 'm', 'a', 'r', 'Raj']

print(c)  # diff between append and extend is extend add as individual list.

print(c.pop())
print(c.pop())

'''g=[]
print(g.pop()) # IndexError: pop from empty list'''

x=[1,2,3,55]
x.remove(55)
print(x)
