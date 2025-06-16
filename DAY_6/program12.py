#checkbutton

import tkinter as tk

window=tk.Tk()

window.title("checkbutton")
window.geometry('800x200')



#create a scale widget 
check_var=tk.BooleanVar()

checkbutton = tk.Checkbutton(window,text="check me",variable=check_var)
checkbutton.pack()


window.mainloop()

