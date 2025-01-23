import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, "You: " + message + "\n")
            self.chat_area.config(state='disabled')
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

    