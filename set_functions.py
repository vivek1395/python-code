var={2,3,5,5,5,44}
print(var)
print(type(var))

var.add(-2)
print(var,id(var))

new_var={55,66,77}
var.update(new_var)
print(var)

new_var1={100,200}

var.update(new_var1,range(7,40,7))
print(var,id(var))

backup_var=var.copy()
print(backup_var,id(backup_var))
print(var.pop())
print(var)

var.remove(100)  ## remove takes only one arguement.
print(var)

var.discard(500) # discard() does not throw error when when object is not find while remove() does.
print(var)

var.clear() # it deletes all the elements from the set.

print(var) ## it will show the emplty set because of clear() functions.


