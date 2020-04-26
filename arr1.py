from array import *

arr= array('i',[])
print(arr)

n= int(input("enter the lenght of array:"))

for a in range(n):
    x=int(input("enter a number:"))
    arr.append(x)
print(arr)

key=int(input("enter the value which you want to search it:"))
k=0
for i in arr:
    if i==key:
        print(i)
        break
    k=k+1
print(k)