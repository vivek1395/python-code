# write a program to find the sum of first n numbers using while loop and pass the number as a argument.

from sys import argv
n=int(argv[1])
i=0
sum=0
while(i<n):
    sum=sum + i
    i=i + 1
print("sum is:",sum)
