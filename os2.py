import os

'''for dirpath,dirnames,filenames in os.walk('.'):
    print("Current Directory Path:",dirpath)
    print("Directories:",dirnames)'''

print(os.getcwd())
os.chdir('C:\\Users\EPCQT\PycharmProjects\\file')
for dirpath,dirnames,filenames in os.walk('.'):
    print("Current Directory Path:",dirpath)
    print("Directories:",dirnames)

