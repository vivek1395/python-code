'''function aliasing is nothing but we create a new function with the same feature .only name will be different.
even the address of both the function will be same.If we change the logic of one function another will also get change'''

def wish(msg,name):
    print(msg,name)
greet=wish    # This is called function aliasing.

greet('good morning','vivek')
wish('Good night','Vishal')
print(id(wish))   # here function is working as a object.16096184
print(id(greet)) # here function is working as a object. 16096184

# Note:- Every function is also an object.

# Even if we delete a one function then still second will be working:
del wish
greet('hello','vivek')
wish('hello','vishal')  #NameError: name 'wish' is not defined