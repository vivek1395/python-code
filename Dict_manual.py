# write a program to enter the name and marks in the dictionary for the number of students.

n=int(input('enter the number of students:'))
d={}

for i in range(1,n+1):
    d[input('enter the name:')]=int(input('enter the marks:'))
print('name and marks is:',d)
