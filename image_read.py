import sys,os

x=os.path.isfile('C:\\Users\EPCQT\PycharmProjects\\file\index.jpg')
if x==True:
    print('file is exist')
else:
    print('file does not exist')
f=('C:\\Users\EPCQT\PycharmProjects\\file\index.jpg','rb')

print(f)