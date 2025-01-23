import tkinter as tk
from tkinter import colorchooser
from tkinter import simpledialog  # Import for asking brush size

class PaintApp:
    def __init__(self, root):
        self.root = root  # Store the root window in the instance
        self.root.title("Paint Application")  # Set the title of the application
        
        self.color = "black"  # Default brush color
        self.brush_size = 5  # Default brush size
        
        # Create a canvas widget to paint on, set initial background to white
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Make the canvas fill available space
        
        # Bind the mouse movement to painting function (left-click drag to draw)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # Set up the menu bar with options
        self.setup_menu()
        
    def setup_menu(self):
        # Create the menu bar and configure it to the root window
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        # Create the 'File' menu and add a 'Clear' option
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear", command=self.clear_canvas)
        
        # Create the 'Brush' menu with options for size and color
        brush_menu = tk.Menu(menu)
        menu.add_cascade(label="Brush", menu=brush_menu)
        brush_menu.add_command(label="Brush Size", command=self.choose_brush_size)  # Set brush size
        brush_menu.add_command(label="Brush Color", command=self.choose_color)  # Set brush color
        
    def paint(self, event):
        # Draw an oval (circle) on the canvas at the mouse position (event.x, event.y)
        # Use the brush size to determine the size of the oval
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)  # Top-left corner
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)  # Bottom-right corner
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)  # Draw the circle
        
    def clear_canvas(self):
        # Clear everything from the canvas
        self.canvas.delete("all")
        
    def choose_brush_size(self):
        # Prompt the user to enter a new brush size via a dialog box
        size = simpledialog.askinteger("Brush Size", "Enter brush size:", initialvalue=self.brush_size)
        if size:
            self.brush_size = size  # Update the brush size with the entered value
            
    def choose_color(self):
        # Prompt the user to choose a color from the color chooser dialog
        color = colorchooser.askcolor(color=self.color)[1]  # [1] gives the hex color code
        if color:
            self.color = color  # Update the brush color with the chosen color

if __name__ == "__main__":
    root = tk.Tk()  # Create the root Tkinter window
    app = PaintApp(root)  # Instantiate the PaintApp class
    root.mainloop()  # Run the Tkinter main loop to display the app
