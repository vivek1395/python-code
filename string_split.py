# we can split the string by using split function by using specified sepeartor
s='vivek loves python'
s1,s2,s3=s.split() # default separator is space for split function
print(s1)
print(s2)
print(s3)

for i in s.split():
    print(i)

date='03-jan-2019'

for j in date.split('-'):
    m=print(j,end=',')
m=str(m)
print(type(m))
print(m)
day,month,year=m.split(',')
print("day is:",day)
print("month is :",month)
print("year is:",year)