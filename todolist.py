import os
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task != "":
        tasks.append({"task": task, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def mark_undone():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = False
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as not done.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# GUI setup
window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x450")

# Entry field
task_entry = tk.Entry(window, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons
tk.Button(window, text="Add Task", width=20, command=add_task).pack(pady=2)
tk.Button(window, text="Mark as Done", width=20, command=mark_done).pack(pady=2)
tk.Button(window, text="Mark as Not Done", width=20, command=mark_undone).pack(pady=2)
tk.Button(window, text="Remove Task", width=20, command=remove_task).pack(pady=2)

# Listbox
task_listbox = tk.Listbox(window, width=45, height=15, font=("Arial", 11))
task_listbox.pack(pady=20)

# Start the app
window.mainloop()