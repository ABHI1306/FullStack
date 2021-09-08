def decorate(func):
    def inner():
        print("In Inner function")
        func()
        print("func() has been called")
    return inner

@decorate
def outer():
    print("In outer function")

#outer = decorate(outer)
outer()