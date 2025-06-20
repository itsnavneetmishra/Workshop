# This is program23.py
import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "×":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("350x250")
root.resizable(False, False)

# Styling
font_style = ("Arial", 12)
bg_color = "#f0f0f0"
button_color = "#e1e1e1"

root.configure(bg=bg_color)

# Number 1 Entry
label_num1 = tk.Label(root, text="First Number:", bg=bg_color, font=font_style)
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root, font=font_style, justify="center")
entry_num1.pack(pady=5)

# Operation Selection
operation_var = tk.StringVar(value="+")  # Default operation

operations_frame = tk.Frame(root, bg=bg_color)
operations_frame.pack(pady=5)

operations = ["+", "-", "×", "÷"]
for op in operations:
    rb = tk.Radiobutton(
        operations_frame,
        text=op,
        variable=operation_var,
        value=op,
        bg=bg_color,
        font=font_style
    )
    rb.pack(side="left", padx=5)

# Number 2 Entry
label_num2 = tk.Label(root, text="Second Number:", bg=bg_color, font=font_style)
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root, font=font_style, justify="center")
entry_num2.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate,
    bg=button_color,
    font=font_style,
    width=15
)
calculate_button.pack(pady=10)

# Result Display
result_label = tk.Label(root, text="Result: ", bg=bg_color, font=font_style)
result_label.pack(pady=10)

# Run the application
root.mainloop()
