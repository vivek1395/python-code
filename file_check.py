# Write a program to check whether the file is exist or not. If it exists then print its content.
import os
x=os.path.isfile('C:\\Users\EPCQT\PycharmProjects\\file\lettr.txt')
if x==True:
    print('file is exist')
    with open('C:\\Users\EPCQT\PycharmProjects\\file\letter.txt','r') as f:
        print(f.read())
else:
    print('File not exist')