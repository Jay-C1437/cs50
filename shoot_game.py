import tkinter as tk  # Importing the tkinter library for GUI.
import random  # Importing random module to generate random target positions.

# Define the ShooterGame class.
class ShooterGame:
    def __init__(self, root):
        # Initialize the main game window.
        self.root = root
        self.root.title("Shooter Game")  # Set the title of the window.
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")  # Create a canvas for the game.
        self.canvas.pack()  # Display the canvas.

        # Create the player as a blue rectangle.
        self.player = self.canvas.create_rectangle(370, 550, 430, 580, fill="blue")
        self.bullets = []  # List to keep track of bullets.
        self.targets = []  # List to keep track of targets.

        # Bind keyboard events for player movement and shooting.
        self.root.bind("<Left>", self.move_left)  # Move player left when the Left arrow key is pressed.
        self.root.bind("<Right>", self.move_right)  # Move player right when the Right arrow key is pressed.
        self.root.bind("<space>", self.shoot)  # Shoot when the spacebar is pressed.

        self.create_targets()  # Create initial targets.
        self.update_game()  # Start updating the game continuously.

    def move_left(self, event):
        # Move the player rectangle 20 pixels to the left.
        self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        # Move the player rectangle 20 pixels to the right.
        self.canvas.move(self.player, 20, 0)

    def shoot(self, event):
        # Create a bullet above the player and add it to the bullets list.
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(x1 + 25, y1 - 10, x2 - 25, y1, fill="yellow")
        self.bullets.append(bullet)

    def create_targets(self):
        # Generate 5 random targets as red rectangles.
        for i in range(5):
            x = random.randint(50, 750)  # Random x-coordinate within the canvas width.
            y = random.randint(50, 300)  # Random y-coordinate within a limited height.
            target = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="red")
            self.targets.append(target)  # Add target to the targets list.

    def update_game(self):
        # Move bullets upward and check for collisions with targets.
        for bullet in self.bullets[:]:  # Iterate over a copy of the bullets list.
            self.canvas.move(bullet, 0, -10)  # Move the bullet up by 10 pixels.
            if self.canvas.coords(bullet)[1] < 0:  # If bullet goes out of bounds:
                self.canvas.delete(bullet)  # Remove it from the canvas.
                self.bullets.remove(bullet)  # Remove it from the bullets list.

        # Check if any bullet hits a target.
        for target in self.targets[:]:
            for bullet in self.bullets:
                if self.check_collision(bullet, target):  # If there is a collision:
                    self.canvas.delete(target)  # Remove the target from the canvas.
                    self.canvas.delete(bullet)  # Remove the bullet from the canvas.
                    self.targets.remove(target)  # Remove the target from the list.
                    self.bullets.remove(bullet)  # Remove the bullet from the list.
                    break  # Exit the loop once a collision is detected.

        # Schedule the next game update.
        self.root.after(50, self.update_game)

    def check_collision(self, bullet, target):
        # Check if the bullet and target rectangles overlap.
        bullet_coords = self.canvas.coords(bullet)
        target_coords = self.canvas.coords(target)
        return (bullet_coords[2] > target_coords[0] and
                bullet_coords[0] < target_coords[2] and
                bullet_coords[3] > target_coords[1] and
                bullet_coords[1] < target_coords[3])

    def auto_shoot(self):
        # Automatically shoot bullets every 500 milliseconds.
        self.shoot(None)
        self.root.after(500, self.auto_shoot)

    def spawn_targets(self):
        # Continuously spawn targets until there are 5 on the canvas.
        if len(self.targets) < 5:
            x = random.randint(50, 750)
            y = random.randint(50, 300)
            target = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="red")
            self.targets.append(target)
        self.root.after(2000, self.spawn_targets)  # Repeat every 2 seconds.

if __name__ == "__main__":
    # Create the main window and run the game.
    root = tk.Tk()
    game = ShooterGame(root)
    game.auto_shoot()  # Start auto-shooting.
    game.spawn_targets()  # Start spawning targets.
    root.mainloop()  # Start the Tkinter event loop.

    def move_targets(self):
        # Move targets downward and check if any reach the bottom.
        for target in self.targets[:]:
            self.canvas.move(target, 0, 5)  # Move target down by 5 pixels.
            if self.canvas.coords(target)[3] > 600:  # If the target reaches the bottom:
                self.game_over()  # End the game.
                return
        self.root.after(100, self.move_targets)  # Schedule the next movement.

    def game_over(self):
        # Display "GAME OVER" and disable controls.
        self.canvas.create_text(400, 300, text="GAME OVER", fill="white", font=("Helvetica", 30))
        self.root.unbind("<Left>")  # Disable left movement.
        self.root.unbind("<Right>")  # Disable right movement.
        self.root.unbind("<space>")  # Disable shooting.

    game.move_targets()  # Start moving the targets.
