'''d={x:x**2 for x in range(1,11)}
print(d,id(d))
d1=d.copy()
print(d1)
d1=d1.fromkeys('4',3)
print(d1)
'''
print('-----------------------------------------------------')

a=['a','b','c']
b=['1','2','3']
c=dict.fromkeys(a,b)
print(c)
print(dir(c))

print(c.popitem())
print(c)
print(c.popitem())
print(c)