# write a program to access each character of string in forward and backward direction by using while loop.

s='vivek loves python' # declaring string
n=len(s)               # calculating length of string
i=0                    # intializing the counter
while (i<n+1):
    for x in s: # reading the string forward direction
        print(x,end=',')
        i=i+1
    print('forward printing completed')
    for y in s[::-1]:  # reading the string in backward direction
        print(y,end=',')
    print('back ward printing completed')

