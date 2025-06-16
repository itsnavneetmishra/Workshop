from tkinter import *
window = Tk()

window.title("Navneet")


def button_clicked():
    print("Button Clicked!")

button = Button(window, text="Hello click me !",command=button_clicked)


button.pack(padx=30,pady=30)
button = Button(window,text="@nd button")
button.pack(padx=30,pady=30)
window.mainloop()