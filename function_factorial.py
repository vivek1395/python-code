# write a function to find the factorial of a given integer:

def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(n-i)
    print('fcatorial of',n, 'is:',fact)
factorial(int(input('enter the number to get the factorial number:')))