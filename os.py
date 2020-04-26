import os as o
print(o.getcwd()) # this will tell you the current directory.

o.chdir('C:\\Users\EPCQT\PycharmProjects\\file')
print(o.getcwd())
'''print(o.listdir('C:\\Users\EPCQT\PycharmProjects\\file'))''' # this is to see the sub-directories inside a directory

w=o.walk('C:\\Users\EPCQT\PycharmProjects\\file') # walk function is to see the content of inside the subdirectory/directory.
for i in w:
    print(i)



