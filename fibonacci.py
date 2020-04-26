#write a program to print fibonacci series.
n=10
def fibonacci():
    a=0
    b=1
    global n
    while (n>0):
        sum=a+b
        yield a,b,a+b
        a=b
        b=sum
        n=n+1
f=fibonacci()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

