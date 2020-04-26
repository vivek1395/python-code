# write a program to create a dictionary which contains their key values square.
# method-1: using for loop
dict={}

for i in range(1,11):
    dict[i]=i**2

print('using for loop:',dict)

# Method-2: using dict comprehension:

dict={i:i**2 for i in range(1,11)}
print('using dict comprehension:',dict)
