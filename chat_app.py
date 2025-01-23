import tkinter as tk  # Import the Tkinter library for GUI development
from tkinter import scrolledtext  # Import ScrolledText widget for a scrollable text area

class ChatApp:
    def __init__(self, root):
        """
        Initialize the chat application.
        """
        self.root = root
        self.root.title("Chat App")  # Set the title of the main application window

        # Create a scrollable text area for displaying chat messages
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        # Wrap text at word boundaries and disable editing
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # Add padding and make it fill both width and height of the window

        # Create an entry widget for the user to type messages
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill=tk.X, expand=True)  # Fill width of the window
        self.entry.bind("<Return>", self.send_message)  # Bind the Enter key to send messages

        # Create a button to send messages
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        # The command specifies the function to be called when the button is clicked
        self.send_button.pack(padx=10, pady=10)  # Add padding around the button

    def send_message(self, event=None):
        """
        Handle sending a message when the button is clicked or Enter is pressed.
        """
        message = self.entry.get()  # Get the text entered in the entry widget
        if message:  # Check if the message is not empty
            self.chat_area.config(state='normal')  # Allow modifications to the chat area
            self.chat_area.insert(tk.END, "You: " + message + "\n")  # Add the message to the chat area
            self.chat_area.config(state='disabled')  # Disable editing again
            self.entry.delete(0, tk.END)  # Clear the entry widget for the next message

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Create an instance of the ChatApp class
    app = ChatApp(root)
    # Start the Tkinter event loop
    root.mainloop()
# Run the chat application
    