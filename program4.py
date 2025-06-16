from datetime import datetime

def not_during_night(func):
    def inner():
        current_hour=datetime.now().hour
        if 7 <= current_hour < 22:
            func()

        else:
            print("sorry ! Unable to play music at nigh")

    return inner

@not_during_night
def music():

    print("Playing Music")

music()