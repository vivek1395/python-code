result=1
def factorial(n):
    global result
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
factorial(int(input('enter a number:')))
print('the factorial value of is:',result)