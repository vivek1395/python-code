'''reduce function reduces the sequence into a single element by applying some functions/logic'''
# syntax: reduce(function,sequence)

# reduce function available in library 'functools' hence we should import functools library before using it.

import functools
s=functools.reduce(lambda x,y:x+y, range(1,int(input('enter a number:')) +1))
print(type(s))  ## int
print(s)

factorial=functools.reduce(lambda x,y:x*y ,range(1,int(input('enter a number:')) +1))
print(factorial)