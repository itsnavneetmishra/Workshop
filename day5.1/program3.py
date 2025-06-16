def decor(func):
    def inner():
        print("----------------------------1-")
        func()
        print("----------------------------2-")

    return inner

@decor
def msg():
    print("Python Programming")


msg=decor(msg)
msg()