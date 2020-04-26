# Syntax to open the file:  f = open(filename, mode)

'''
r= read mode, this will only read data. if the file is not present then it will give file not found error.
w= Write mode, this will write data on the file. it will overwrite the previous data, this means you will lost
  your previous data. If the file is not present then it will create new file.
a= append mode, this will append data on the existing file. If the file is not present then it will create a new file.
r+ = it will read and write data into file. This mode won't override the data.
w+= It reads and writes the data into file. It will override the previous data.
a+= it read and append the data from the existing file. It wont overide the data.
x= it create a new file if the file is not present. and if the file is present it will throw FileExistsErrors.

All the modes are only applicable to text files and not on binary files.
for binary file use the below modes.
rb: read binary files
wb: write binary files
ab: append binary files
r+b: read,write on binary files
w+b: read and write on binary files.it overrides.
a+b: it read and append the data. It wont override.
xb: It create a binary file if the file is not exist. if it exists then it will give FileExistError.

'''
import os
f=open("C:\\Users\EPCQT\PycharmProjects\File\letter.txt",'r')
count=0
for i in f.readlines():
    print(i)
    count=count +1

print(os.stat("C:\\Users\EPCQT\PycharmProjects\File\letter.txt"))
f.close()
print('total no. of rows in this file:',count)

'''st_mode==>Protection Bits
st_ino==>Inode number
st_dev===>device
st_nlink===>no of hard links
st_uid===>userid of owner
st_gid==>group id of owner
st_size===>size of file in bytes
st_atime==>Time of most recent access
st_mtime==>Time of Most recent modification
st_ctime==> Time of Most recent meta data change'''

stats=os.stat("C:\\Users\EPCQT\PycharmProjects\File\letter.txt")
print("File Size in Bytes:",stats.st_size)
