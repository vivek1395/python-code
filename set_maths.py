a={1,2,3,4}
b={3,4,5,6}

print('union of a and b is',a.union(b))

print('intersection of a and b is:',a.intersection(b))

print('a -b is :',a.difference(b))

print('a-b or b-a is:',a.symmetric_difference(b))

print('100' in a) ## False

print(1 in a) ## True
print('1' in a) ## False
