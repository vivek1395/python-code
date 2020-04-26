def cal(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    rem=x%y
    return  sum,sub, mul, div,rem
t=cal(int(input('enter first number:')),int(input('enter second number:')))
print(t)
print(type(t))
s=['sum','sub','div','mul','rem']
i=0
while(i<len(t)):
    print(s[i],'=',t[i])
    i=i+1
