
# Method-1:
s='vivek loves python'

a,b,c=[str(i) for i in s.split(' ')]
print(a[::-1] + ' ' + b[::-1] + ' ' + c[::-1])

# Method-2:

n=s.split()
print(s)




