#horizontal button


import tkinter as tk

window=tk.Tk()

window.title("scale example")
window.geometry('800x200')



#create a scale widget 

scale=tk.Scale(window , from_=0 , to=100 , orient=tk.HORIZONTAL)
scale.pack()


window.mainloop()

