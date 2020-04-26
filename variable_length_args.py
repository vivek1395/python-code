def sum(*n):
    total_sum=0
    print(n,type(n))
    for i in n:
        total_sum=total_sum +i
    print('total sum is:',total_sum)
    return total_sum

sum(10,20,30,4,5)

