import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x200")
label = tk.Label(root, text="Hello from Tkinter!", font=("Arial", 14))
label.pack(pady=40)
root.mainloop()
