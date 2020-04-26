x=[x for x in range(10)]
print('type of x var is:', type(x), x)  # <class 'list'>

y=[y**2 for y in range(11)]
print(y)  ## [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

z=( i**3 for i in range(11))
print(type(z))

p=list(z)
print(type(p))
print('here we go:',p)

# Note: once iterate the generator and if we re-iterate again then generator will be empty.

for i in z:
    print('empty:',i)  ## here it will give empty . there will no data in z.



