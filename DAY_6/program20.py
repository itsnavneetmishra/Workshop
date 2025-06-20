
from tkinter import *
from tkcalendar import DateEntry

root = Tk()
root.title("Date Picker Example")
root.geometry('800x200')

# Create a DateEntry widget
date_entry = DateEntry(root)
date_entry.pack()

root.mainloop()