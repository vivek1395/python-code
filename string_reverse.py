s='vivek loves python'
print('string is:',s)

# method-1 : using string slicing operator

rs1=s[::-1]
print('reverse string is:',rs1)

# method-2: using join operator

rs2=''.join(reversed(s))
print('reverse string is:',rs2)

# method-3: using for loop
i=len(s) -1
rs3=''

while(i>=0):
    rs3= rs3 + s[i]
print(rs3)


