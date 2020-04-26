import sys,os
x= os.path.isfile('C:\\Users\EPCQT\PycharmProjects\\file\letter.txt')
wcount=ccount=lcount=0
if x==True:
    print('File exist')
    f=open('C:\\Users\EPCQT\PycharmProjects\\file\letter.txt','r')
else:
    print('File not exist')
for i in f:
    lcount=lcount + 1
    ccount=ccount + len(i)
    words=i.split()
    wcount=wcount + len(words)

print('no. of lines:',lcount)
print('no. of charachers:',ccount)
print('no. of words:',wcount)

