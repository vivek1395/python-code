# write a program to print the * in the form pyramid shape (also known as equivalent triangle)


from sys import argv
n=int(argv[1])
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print((i)*"* ")
print("Chan this xmas tree for you enjoy")

