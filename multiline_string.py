x="hello 'vivek'"
print(x)
y='hello "vivek"'
print(y)
z='''bye 
      vivek
      see you soon''' # defining multi-line strings.
print(z)
del x # deleting the variable for garbage collection
del y # after deleting you wont be able to access this variable
z=None # it only delete the value but still you will able to acces the variable
print(z) # it will print None
print(x)
print(y)

