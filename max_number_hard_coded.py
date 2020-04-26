# write a program to find the maximum number given to 3 numbers.

from sys import argv
args=argv[1:]
if (argv[1]> argv[2] and argv[1]>argv[3]):
    print("max number is:" ,argv[1])
elif (argv[2]>argv[3]):
    print("max number is:",argv[2])
else:
    print("max number is:",argv[3])


