'''f=open("C:\\Users\EPCQT\PycharmProjects\File\letter.txt","r")
l=["vivek\n","vishal\n","Gagana\n"]
print(f.read(3))
print('next records')
print(f.read())
f.close()'''

with open("C:\\Users\EPCQT\PycharmProjects\File\letter.txt","r") as f:
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    print(f.seek(0))
    print(f.read(5))