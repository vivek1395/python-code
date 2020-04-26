# Write a lambda function to find the even number using filter function.
# syntax of filter function: filter(function, sequence)
# here we can see lambda is a function and range is used as sequence. you can use string, list ,tuple etc as a sequence.

even_no=tuple(filter(lambda x:x%2==0,range(1,20))) # here tuple is converting from range into tuple.
# and then if the condition is satisfied then it is selecting those elements.
print(even_no)
print(type(even_no))