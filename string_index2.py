s='vivek loves python'

try:
    n=s.index('z')
except ValueError:
    print('Substring not found')
else:
    print('substring found')
finally :
    print('finally run in every situation whether error occurred or not')