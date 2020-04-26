import sys

args= sys.argv[1:]
count=0
sum=0

for x in args:
    count=count +1
    sum=sum + int(x)

print("total no. of arguments:", count)
print("total sum is :",sum)
