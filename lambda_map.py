'''map function is used to apply some logic/function on each element in the given sequence and
produce some new modified elements for the every elements
syntax: map(function,sequence)      '''

# write a program to get the square of each element from a sequence using lambda and map fucnctions:

s=list(map(lambda x:x**2, range(1,5)))
print(s)

