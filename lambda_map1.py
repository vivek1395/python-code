'''we can use many sequence in map function but the condition is length of both the sequence should be same.'''

a=[1,2,3,4]
b=['vivek','vishal','Neha','Fruity']
c=[2,3,4,5]

s=list(map(lambda a,b: str(a) +'='+ str(b),a,b))
print(type(s),s)
r=list(map(lambda a,c:a*c,a,c))
print(r)