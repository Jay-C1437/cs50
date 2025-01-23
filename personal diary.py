import tkinter as tk
import tkinter.font as tkFont  # Import font module for custom fonts
from tkinter import messagebox  # For displaying message boxes
from datetime import datetime  # Import datetime for date handling

class PersonalDiary:
    def __init__(self, root):
        self.root = root  # Store the root window in the instance
        self.root.title("Personal Diary")  # Set the title of the application
        self.root.geometry("500x500")  # Set the window size
        self.root.configure(bg="#f0f0f0")  # Set the background color of the window

        # Title label displaying the name of the app
        self.title_label = tk.Label(root, text="Personal Diary", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)  # Add padding around the title label

        # Frame to hold the date entry and diary text entry
        self.entry_frame = tk.Frame(root, bg="#f0f0f0")
        self.entry_frame.pack(pady=10)  # Add padding around the frame

        # Date label and entry field
        self.date_label = tk.Label(self.entry_frame, text="Date:", font=("Helvetica", 12), bg="#f0f0f0")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)  # Position using grid
        self.date_entry = tk.Entry(self.entry_frame, font=("Helvetica", 12))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)  # Position using grid
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Set default to today's date

        # Label and text entry for the diary entry
        self.text_label = tk.Label(self.entry_frame, text="Diary Entry:", font=("Helvetica", 12), bg="#f0f0f0")
        self.text_label.grid(row=1, column=0, padx=5, pady=5)  # Position using grid
        self.text_entry = tk.Text(self.entry_frame, width=40, height=10, font=("Helvetica", 12))  # Text box for diary entry
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)  # Position using grid

        # Button to save the diary entry
        self.save_button = tk.Button(root, text="Save Entry", font=("Helvetica", 12), command=self.save_entry)
        self.save_button.pack(pady=10)  # Add padding around the save button

    def save_entry(self):
        # Get the date and text entered by the user
        date = self.date_entry.get()
        text = self.text_entry.get("1.0", tk.END).strip()  # Get all the text from the text widget

        # Check if both fields are filled in
        if not date or not text:
            messagebox.showwarning("Warning", "Please fill out all fields")  # Show warning if fields are empty
            return

        # Append the entry to the diary.txt file
        with open("diary.txt", "a") as file:
            file.write(f"{date}\n{text}\n\n")  # Write the date and entry to the file

        # Show a success message and clear the form
        messagebox.showinfo("Success", "Diary entry saved successfully")
        self.date_entry.delete(0, tk.END)  # Clear the date entry field
        self.text_entry.delete("1.0", tk.END)  # Clear the text entry field
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Set the date entry to today's date again

if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    app = PersonalDiary(root)  # Create an instance of the PersonalDiary class
    root.mainloop()  # Run the Tkinter main loop to display the app
