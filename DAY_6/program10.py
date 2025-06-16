#horizontal button


import tkinter as tk

window=tk.Tk()

window.title("spin box")
window.geometry('800x200')



#create a scale widget 

spinbox=tk.Spinbox(window , from_=0 , to=10  )
spinbox.pack()


window.mainloop()

