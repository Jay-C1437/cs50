import tkinter as tk
from tkinter import messagebox
import webbrowser


class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie App")
        self.root.geometry("600x400")

        self.movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]

        self.label = tk.Label(root, text="Welcome to Movie App", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.listbox = tk.Listbox(root, font=("Helvetica", 14))
        self.listbox.pack(pady=20)

        for movie in self.movies:
            self.listbox.insert(tk.END, movie)

        self.watch_button = tk.Button(root, text="Watch", command=self.watch_movie, font=("Helvetica", 14))
        self.watch_button.pack(pady=20)

    def watch_movie(self):
        selected_movie = self.listbox.get(tk.ACTIVE)
        if selected_movie:
            messagebox.showinfo("Watch Movie", f"Now watching: {selected_movie}")
        else:
            messagebox.showwarning("Warning", "Please select a movie to watch")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()

    def watch_movie(self):
        selected_movie = self.listbox.get(tk.ACTIVE)
        movie_links = {
            "Inception": "https://www.youtube.com/watch?v=8hP9D6kZseM",
            "The Matrix": "https://www.youtube.com/watch?v=vKQi3bBA1y8",
            "Interstellar": "https://www.youtube.com/watch?v=zSWdZVtXT7E",
            "The Dark Knight": "https://www.youtube.com/watch?v=EXeTwQWrcwY",
            "Pulp Fiction": "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
        }
        if selected_movie:
            link = movie_links.get(selected_movie)
            if link:
                webbrowser.open(link)
                messagebox.showinfo("Watch Movie", f"Now watching: {selected_movie}")
            else:
                messagebox.showerror("Error", "Link not found for the selected movie")
        else:
            messagebox.showwarning("Warning", "Please select a movie to watch")

            