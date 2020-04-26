table_2=[]
table_3=[]
table_4=[]
table_5=[]
table_6=[]
table_7=[]
others=[]
for i in range(50):
    if (i%2==0):
        table_2.append(i)
    elif (i%3==0):
        table_3.append(i)
    elif (i%4==0):
        table_4.append(i)
    elif (i%5==0):
        table_5.append(i)
    elif (i%6==0):
        table_6.append(i)
    else:
        others.append(i)
print("table of 2 is:",table_2)
print("table of 3 is:",table_3)
print("table of 4 is",table_4)
print("table of 5 is:",table_5)
print("table of 6 is:",table_6)
print("remainders records:",others)
