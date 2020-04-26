s='vivek loves python'

print(s.find('v')) # output is 0
print(s.index('v')) # output is 0

print(s.find('z')) # output is -1
print(s.index('z')) # output : valueError : substring not found : this is the only difference between find and index
# while searching substring using index function if string not found then it throws error.

