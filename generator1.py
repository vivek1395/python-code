'''To create a generator we use a yield keyword and to get the value we use a next keyword.'''

'''def gen():
    yield 'a'
    yield 'b'
    yield 'c'
g=gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))'''

def countdown(num):
    print('countdown starts...')
    while(num>0):
        yield num
        num=num - 1
c=countdown(5)
'''for i in c:
    print(i)'''

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c)) ##this print statement will give error.StopIteration


