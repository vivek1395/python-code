t=(x**2 for x in range(1,6))
print(type(t))   # <class 'generator'>

for i in t:
    print(i,end=' ')