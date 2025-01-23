import tkinter as tk  # Import the tkinter module for GUI creation.
from tkinter import messagebox  # Import messagebox for showing alerts.
import webbrowser  # Import webbrowser to open movie links in the default browser.

# Define the MovieApp class.
class MovieApp:
    def __init__(self, root):
        # Initialize the main window.
        self.root = root
        self.root.title("Movie App")  # Set the title of the app window.
        self.root.geometry("600x400")  # Set the dimensions of the window.

        # List of available movies.
        self.movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]

        # Label for the app heading.
        self.label = tk.Label(root, text="Welcome to Movie App", font=("Helvetica", 16))
        self.label.pack(pady=20)  # Add some padding around the label.

        # Listbox to display the list of movies.
        self.listbox = tk.Listbox(root, font=("Helvetica", 14))
        self.listbox.pack(pady=20)  # Add padding around the listbox.

        # Add each movie to the listbox.
        for movie in self.movies:
            self.listbox.insert(tk.END, movie)

        # Button to watch the selected movie.
        self.watch_button = tk.Button(root, text="Watch", command=self.watch_movie, font=("Helvetica", 14))
        self.watch_button.pack(pady=20)  # Add padding around the button.

    def watch_movie(self):
        # Fetch the currently selected movie from the listbox.
        selected_movie = self.listbox.get(tk.ACTIVE)

        # Dictionary mapping movies to their respective YouTube trailer links.
        movie_links = {
            "Inception": "https://www.youtube.com/watch?v=8hP9D6kZseM",
            "The Matrix": "https://www.youtube.com/watch?v=vKQi3bBA1y8",
            "Interstellar": "https://www.youtube.com/watch?v=zSWdZVtXT7E",
            "The Dark Knight": "https://www.youtube.com/watch?v=EXeTwQWrcwY",
            "Pulp Fiction": "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
        }

        # Check if a movie is selected.
        if selected_movie:
            link = movie_links.get(selected_movie)  # Get the link for the selected movie.
            if link:
                webbrowser.open(link)  # Open the movie link in the default browser.
                messagebox.showinfo("Watch Movie", f"Now watching: {selected_movie}")  # Show an info message.
            else:
                messagebox.showerror("Error", "Link not found for the selected movie")  # Error if no link is found.
        else:
            messagebox.showwarning("Warning", "Please select a movie to watch")  # Warn if no movie is selected.

# Main block to run the app.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window.
    app = MovieApp(root)  # Instantiate the MovieApp class with the root window.
    root.mainloop()  # Start the Tkinter event loop.
