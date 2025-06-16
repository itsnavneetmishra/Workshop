from tkinter import *
window = Tk()

window.title("Navneet")


def button_clicked():
    button.config(text=" Good Job", bg="red", fg="white")


button = Button(window, text="Hello click me !",command=button_clicked,font=("Arial",50))
button.pack(padx=20,pady=20)


window.mainloop()