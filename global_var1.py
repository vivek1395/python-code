a=10  # this is a global variable
b=20  # this is a global variable
c=30  # this is a global variable
d=40  # this is a global variable
def f1():
    global a  # declaring global variable inside a function.
    print('f1- a is:',a)
    b=99  # this is a local variable
    print('f1-b is:',b)
    c=199  # this is a global variable.
    print('f1-c is:',c)
    global d  # this is global variable
    print('f1-d is:',d)
    d=299
    print('f1-d is :',d)


def f2():
    print('f2:',a) # this will also work as global variable
    print('f2:',b) # this is a global variable
    global c
    print('f2:',c)
    print('f2-d is:',d)
f1()
f2()