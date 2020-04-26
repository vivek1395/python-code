def outer():
    print('outer function executed')
    def inner():
        print('inner function executed')
        def most_inner():
            print('most inner function executed')
        most_inner()
    inner()
outer()