
import tkinter as tk
from tkinter.ttk import Combobox

window=tk.Tk()

window.title("Combobox example")
window.geometry('800x400')

def combobox_selected(event):
    selected_value=combobox.get()
    label.config(text=f"Selected: {selected_value}")


#create a label to display the selected value

label=tk.Label(window,text="Select an option:" )
label.pack(padx=20,pady=20)


#create a Combobox widget 

options =["option 1","option 2","option 3"]
combobox = Combobox(window,values=options)
combobox.pack(padx=20,pady=20)


combobox.bind("<<Combobox selected>>",combobox_selected)

window.mainloop()



from tkinter import *

