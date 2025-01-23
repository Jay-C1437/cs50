import tkinter as tk
import time

# Function to update the stopwatch time
def update_time():
    if running:
        global elapsed_time
        elapsed_time += 1
        time_str = f"{elapsed_time // 600}:{(elapsed_time // 10) % 60:02d}.{elapsed_time % 10}"
        label.config(text=time_str)
    root.after(100, update_time)

# Function to start the stopwatch
def start():
    global running
    running = True

# Function to stop the stopwatch
def stop():
    global running
    running = False

# Function to reset the stopwatch
def reset():
    global elapsed_time
    elapsed_time = 0
    label.config(text="0:00.0")

# Initialize the main window
root = tk.Tk()
root.title("Stopwatch")

# Initialize variables
elapsed_time = 0
running = False

# Create and place the label to display time
label = tk.Label(root, text="0:00.0", font=("Helvetica", 48))
label.pack()

# Create and place the start button
start_button = tk.Button(root, text="Start", command=start)
start_button.pack(side=tk.LEFT)

# Create and place the stop button
stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT)

# Create and place the reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT)

# Call the update_time function to start the time update loop
update_time()

# Add some padding to the buttons and label
label.pack(pady=20)
start_button.pack(side=tk.LEFT, padx=10, pady=10)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)

# Change the background color of the main window
root.configure(bg="lightblue")

# Change the font and color of the label
label.config(font=("Helvetica", 48), bg="lightblue", fg="white")

# Change the style of the buttons
start_button.config(font=("Helvetica", 14), bg="green", fg="white", relief="raised", bd=5)
stop_button.config(font=("Helvetica", 14), bg="red", fg="white", relief="raised", bd=5)
reset_button.config(font=("Helvetica", 14), bg="yellow", fg="black", relief="raised", bd=5)

# Start the Tkinter event loop
root.mainloop()

