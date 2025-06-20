#generating list boxes



import tkinter as tk


window=tk.Tk()

window.title("List box example")
window.geometry('400x400')

listbox=tk.Listbox(window)

listbox.insert(1,"Option 1")
listbox.insert(2,"option 2")
listbox.insert(3,"option 3")
listbox.insert(4,"option 4")
listbox.pack()




window.mainloop()