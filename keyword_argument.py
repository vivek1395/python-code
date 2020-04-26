def wish(name,msg):
    print("Hello",name,msg)
wish(msg='good morning',name='vivek')
wish(name='vivek',msg='good morning')
wish('vivek','Good morning')
wish('Good morning','Vivek')  # positional argument in wrong order hence result get wrong but executed.
#wish('vivek') #TypeError: wish() missing 1 required positional argument: 'msg'
wish('vivek',msg='Good Morning') # we are passing both positional and keyword arguments simultaneously.

wish(name='vivek','Good Morning') # SyntaxError: positional argument follows keyword argument
# so we should always give first positional argument if we are passing both positional and keyword arguments.