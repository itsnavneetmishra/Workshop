def decor(func):
    def inner():
        print("-----------------------------")
        func()
        print("-----------------------------")

    return inner


def msg():
    print("Python Programming")


msg=decor(msg)
msg()