from itertools import zip_longest

vacancy=range(1,6)
emp=['vivek','himadri','chan']
tech=['python','Step function','S3','EC2']

z=zip_longest(vacancy,emp,tech,fillvalue='?')
for i in z:
    print(i)