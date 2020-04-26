from array import *
arr= array('i',[1,33,44,65,33])
print(arr)

n=len(arr)  # it will give the length of array.
print("length of array is :",n)

arr.reverse()
print("reverse string is: ",arr)

print(arr.count(33))  # it will give the no. of occurrence of particular element in a given array.

print(arr.buffer_info()) ## it will give the address of the array and size of the array.
#       (2058945545136, 5)

arr.pop()
print(arr)  # it will delete a element from array.

print(arr[2]) # it will print the value which is present at index 2.

arr.append(100)  # it will append '100' in the existing array at the last index.
print(arr)

arr.extend([222,121]) # adding one array to existing array
print(arr)

arr.extend([500])
print(arr)

arr.insert(2,202)
print(arr)

arr.remove(202)
print(arr)

arr.remove(33) # this only delete the first occurrence not all the occurrence.
print(arr)

brr=arr
print("brr:",brr)

print(id(arr))
print(id(brr))

brr.pop()
print("brr",brr)
print("arr",arr)

newarr= array(arr.typecode, (i for i in arr)) # create a new array similar to existing array whose address will be different.
print("newarr",newarr)

print("arr:",id(arr))
print("newarr:",id(newarr))




