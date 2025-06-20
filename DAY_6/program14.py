#Radio_button

import tkinter as tk

window=tk.Tk()

window.title("Radiobutton")
window.geometry('800x200')



#create a scale widget 
radio_var=tk.BooleanVar()

radiobutton1 = tk.Radiobutton(window,text="Male",variable=radio_var,value="Male")
radiobutton2 = tk.Radiobutton(window,text="Female",variable=radio_var,value="Female")


radiobutton1.pack()
radiobutton2.pack()


window.mainloop()