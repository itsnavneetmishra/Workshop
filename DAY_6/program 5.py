from tkinter import *

# Create the main window which is an object of Tk class
window = Tk()
window.title("Hello, NIET!")



label=Label(window,text="Hello, Navneet Mishra", font=("Arial Bold", 70))
label.config(bg="red",fg="white")
label.pack()

# Start the GUI event Loop
window.mainloop()