import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from datetime import datetime

class PersonalDiary:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        self.title_label = tk.Label(root, text="Personal Diary", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.entry_frame = tk.Frame(root, bg="#f0f0f0")
        self.entry_frame.pack(pady=10)

        self.date_label = tk.Label(self.entry_frame, text="Date:", font=("Helvetica", 12), bg="#f0f0f0")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.entry_frame, font=("Helvetica", 12))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.text_label = tk.Label(self.entry_frame, text="Diary Entry:", font=("Helvetica", 12), bg="#f0f0f0")
        self.text_label.grid(row=1, column=0, padx=5, pady=5)
        self.text_entry = tk.Text(self.entry_frame, width=40, height=10, font=("Helvetica", 12))
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)

        self.save_button = tk.Button(root, text="Save Entry", font=("Helvetica", 12), command=self.save_entry)
        self.save_button.pack(pady=10)

    def save_entry(self):
        date = self.date_entry.get()
        text = self.text_entry.get("1.0", tk.END).strip()

        if not date or not text:
            messagebox.showwarning("Warning", "Please fill out all fields")
            return

        with open("diary.txt", "a") as file:
            file.write(f"{date}\n{text}\n\n")

        messagebox.showinfo("Success", "Diary entry saved successfully")
        self.date_entry.delete(0, tk.END)
        self.text_entry.delete("1.0", tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalDiary(root)
    root.mainloop()