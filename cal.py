import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math error", "Cannot divide by zero.")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")

# Labels and Entry boxes
tk.Label(window, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="Choose operation (+, -, *, /):").pack(pady=5)
operation = tk.Entry(window)
operation.pack()

# Calculate button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Run the app
window.mainloop()

