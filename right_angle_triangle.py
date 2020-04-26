# write a program to print * in the form of right angle triangle.

from sys import argv
n=int(argv[1]) # to take the numbers of rows of *s.
i=1
while(i<n):
    print(i*"*")
    i=i+1