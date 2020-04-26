s='The sun rises in the east'
print(s.startswith('the'))  # output is false

print(s.startswith('The')) # output is true hence case sensitive

print(s.startswith('The sun')) # output is true that means it scan for consecutive words.

print(s.startswith('Th')) # output is true means it checks for prefix

print(s.startswith('sun',4,77)) # output is true as sun start at 4th index

print(s.startswith('sun',4)) # true here scanning start with 4th index till last.


print(s.endswith('east')) # output is true
