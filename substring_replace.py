s='vivek loves java'
print(s)
print(id(s)) # 59857664
s=s.replace('java','python')
print(s)
print(id(s)) # 59857712

# note: since as we know strings are immutable and its look like we are changing the string but its not happening .
# its creating a new object with new address.