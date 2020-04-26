# write a function to check whether a number is odd or even:

def even_or_odd(n):
    if (n%2==0):
        print(n,'is a even number')
    else:
        print(n, 'is a odd number')
even_or_odd(int(input('enter the number:')))