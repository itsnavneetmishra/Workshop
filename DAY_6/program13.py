#Radio_button

import tkinter as tk

window=tk.Tk()

window.title("Radiobutton")
window.geometry('800x200')



#create a scale widget 
radio_var=tk.BooleanVar()

radiobutton = tk.Radiobutton(window,text="check me",variable=radio_var)
radiobutton.pack()
window.mainloop()