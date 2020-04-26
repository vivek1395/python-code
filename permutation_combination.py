# write a function to get the permutation value:

def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(n-i)
    print('fcatorial of',n, 'is:',fact)
    print(type(fact))
    return fact

factorial(int(input('enter the number to get the factorial number:')))

def permutation(n,r):
    p=factorial(n)/factorial(n-r)
    print('permutation value is:',p)
    return p
permutation(int(input('enter the value of n for permutation:')),int(input('enter the value of r for permutation:')))

def combination(n,r):
    c=factorial(n)/(factorial(r)*factorial(n-r))
    print('combination value is :',c)
    return c
combination(int(input('enter the value of n for combination:')),int(input('enter the value of r for combination:')))
