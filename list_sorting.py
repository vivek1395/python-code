l=[1,4,2,84,22,44]
print(id(l))
x=l     ## this is called aliasing of list. here x is the reference variable to the existing list l.

# the problem with the above approach is if we change content of any list list then other will also get change.


print('l',id(l))
print('x',id(x))
x.sort(reverse=False)
print(l,id(l))
print(x,id(l))

#l=[1,4,2,84,22,44,'vivek']
#l.sort()   ## TypeError: '<' not supported between instances of 'str' and 'int'

l=['vivek','sony','abhishek','Navin','VIVEK']
l.sort()
print(l)  ## ['Navin', 'VIVEK', 'abhishek', 'sony', 'vivek']

# to overcome the problem with the aliasing we should do cloning of the object.
# the process of creating an independent object and exactly duplicates records is calling cloning of list.
#methods of cloning:

# Method-1: using slice operator
m=[1,2,3,5,77,33]
n=m[:]
print(m,id(m)) # if we use slice operator then address will be different for both variables.
print(n,id(n))

n.pop()
print(m,id(m))
print(n,id(n))

# method-2: using list copy function

p=[1,2,34,44]
q=p.copy()
print(p,id(p))
print(q,id(q))

q.pop()

print(p,id(p))
print(q,id(q))