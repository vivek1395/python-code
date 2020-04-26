# slice operator >> new_string= string[beging:end: step]

s='vivek loves python'
print(s)
s1=s[1:5]
s2=s[5:]
s3=s[1:14:2]
s4=s[-10:-1]
s5=s[-10:-1:2] # when are we printing string from left to right the step value should be positive
s6=s[:] # it prints all the string.
s7=s[::] # it also print all the string character.
s8=s[::-1] # it reverse the string.
s9=s[-1:-10:-2] # when are we printing string from right to left then step value should be negative.

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)