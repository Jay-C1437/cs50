import tkinter as tk
from tkinter import messagebox

def validate_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name:
        messagebox.showerror("Validation Error", "Name is required")
        return
    if not email:
        messagebox.showerror("Validation Error", "Email is required")
        return
    if not age.isdigit():
        messagebox.showerror("Validation Error", "Age must be a number")
        return

    messagebox.showinfo("Success", "Form submitted successfully")

# Create the main window
root = tk.Tk()
root.title("Form Validator")

# Create and place the labels and entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=validate_form)
submit_button.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()