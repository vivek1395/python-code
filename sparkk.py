if __name__ == '__main__':
    n = int(input("enter the list size:"))
    lis= []
    for i in range(n):
        x=int(input("enter the value:"))
        lis.append(x)
    lissq=[a**2 for a in lis]
    print(lis)
    print(lissq)