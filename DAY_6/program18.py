import tkinter as tk
from tkinter import ttk
# Create the main window
window = tk.Tk()
window.title("Login Form")
window.geometry("350x250")  # Set fixed window size
window.resizable(False, False)  # Disable resizing

def submit_clicked():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:  # Check if both fields are filled
        result_label.config(text="Login successful!", fg="green")
    else:
        result_label.config(text="Please fill all fields!", fg="red")

# Configure style
window.configure(bg="#f0f0f0")
font_style = ("Arial", 10)

# Username section
username_label = tk.Label(window, text="Username:", bg="#f0f0f0", font=font_style)
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(window, font=font_style, width=25)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password section
password_label = tk.Label(window, text="Password:", bg="#f0f0f0", font=font_style)
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(window, show="*", font=font_style, width=25)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(
    window, 
    text="Login", 
    command=submit_clicked,
    bg="#00FF00",  # Green color
    fg="red",
    font=font_style,
    width=15
)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result label
result_label = tk.Label(window, text="", bg="#f0f0f0", font=font_style)
result_label.grid(row=3, column=0, columnspan=2)

# Set focus to username field when window opens
username_entry.focus()

window.mainloop()