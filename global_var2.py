a=10
def f1():
    a=99
    print(a) # this will print the local variables
    print(globals()['a'])  # this will print the global variable
f1()