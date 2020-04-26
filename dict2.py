# write a program to create a dictionary by user and add the sum of values.

d=eval(input('enter the dictionary:'))
print(d)


sum2=sum(d.values())  # method-1
print('sum2 is :',sum2)

'''sum=0

for i in d.values():    # method-2:
    sum=sum + i

print('sum of number is:',sum)'''