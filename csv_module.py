# How to read a csv file.
import csv
f=open('C:\\Users\EPCQT\PycharmProjects\\testfile\\vivek.txt','r+')
r=csv.reader(f)
for i in r:
    print(i)

f=f.writelines('He is a good boy too')
print(f)

print(dir(csv))


