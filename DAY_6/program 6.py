from tkinter import *

window=Tk()

window.title("My first web page")
label=Label(window,text="Navneet Mishra", font=("New Times Roman", 70))
label.config(bg="yellow",fg="red")

label.pack(side="left",pady=150,ipady=50)



window.mainloop()