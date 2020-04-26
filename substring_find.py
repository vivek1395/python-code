# find function find the index of the first occurrence of a substring in a given string.
# by-default  it search in entire string.
# if we want to search from specific point to point we have to give starting point and end point in find function.
# syntax : string.find(substring,begin,end)

s='vivek loves python'
print(s.find('vivek'))  # output is at 0 index

print(s.find('is')) # output is -1 as 'is' not found in string

print(s.find('loves')) # output is at 6 index

print(s.find('Loves')) # output is -1 as Loves not found as find function treat L and l different. It is case-sensitive.

print(s.find('v')) # output is 0 , so we can see it only gives the first occurance of the string
print(s.find('v')) # output is 0
print(s.find('v')) # output is 0
print(s.find('v',5,10))  # here search begins from index 5 and end at index 10.