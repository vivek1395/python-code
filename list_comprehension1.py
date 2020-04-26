l=[(x,y) for x in range(3) for y in range(3)]
print(l)   ## cartesian product due to (x,y)

l=[(x,y) for x in range(3) for y in range(3) if (x==y)]
print(l)

l=[(x,-y) for x in range(3) for y in range(3) if (x==y)]
print(l)

l=[(x,y,z) for x in range(1,10) for y in range(1,10) for z in range(1,10) if (x+y+z==5)]
print('total no. of triplets is:',len(l))
print(l)

l=[(x,y,z) for x in range(1,20) for y in range(1,20) for z in range(1,20) if (x**2 + y**2==z**2)]
print(l)

s='vivek loves python'
a,b,c=[str(x) for x in s.split()]
print('a=',a)
print('b=',b)
print('c=',c)


