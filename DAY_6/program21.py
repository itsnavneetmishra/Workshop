import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Date Picker")
root.geometry("400x300")

# Calendar widget
cal = Calendar(root, selectmode='day', year=2025, month=6, day=16)
cal.pack(pady=20)

# Function to show selected date
def get_date():
    selected = cal.get_date()
    result_label.config(text="Selected Date: " + selected)

# Button to select date
tk.Button(root, text="Get Selected Date", command=get_date).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
