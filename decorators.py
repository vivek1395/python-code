def decor(func):
    def inner(country):
        if country=='india':
            print('Good Morning',country)
        else:
            func(country)
    return inner
def wish(country):
    print('Good Night',country)
df=decor(wish)
df(input('enter the country:'))
