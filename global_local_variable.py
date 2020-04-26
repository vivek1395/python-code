s='vivek kumar'
def f1():
    s='Vishal kumar'
    print(s)
def f2():
    s='Balu'
    print(s)
print(s) ## this will print vivek kumar as this is global variable
f1()  ## this will print vishal kumar
f2() ## this will print Balu
