import tkinter as tk  # Import the tkinter module for creating the GUI.
from tkinter import messagebox  # Import messagebox for showing alerts like winner or tie messages.

# Define the TicTacToe class
class TicTacToe:
    def __init__(self, root):
        # Initialize the main window and game variables.
        self.root = root
        self.root.title("Tic Tac Toe")  # Set the title of the window.
        self.root.resizable(False, False)  # Prevent the window from being resized.
        self.current_player = "X"  # Start with player "X".
        self.board = [""] * 9  # Create an empty game board with 9 cells.
        self.buttons = []  # List to hold the button widgets for the game grid.
        self.create_widgets()  # Call the method to create the game grid.

    def create_widgets(self):
        # Create 9 buttons to represent the Tic Tac Toe grid.
        for i in range(9):
            button = tk.Button(self.root, 
                               text="",  # Initially, the button text is empty.
                               font=("Arial", 24),  # Set the font style and size.
                               width=5, height=2,  # Set the button size.
                               command=lambda i=i: self.on_button_click(i))  # Assign a function for button click.
            button.grid(row=i // 3, column=i % 3)  # Arrange the buttons in a 3x3 grid.
            self.buttons.append(button)  # Add the button to the buttons list.

    def on_button_click(self, index):
        # Handle the event when a button is clicked.
        if self.board[index] == "":  # Check if the cell is empty.
            self.board[index] = self.current_player  # Update the board with the current player's symbol.
            self.buttons[index].config(text=self.current_player)  # Update the button text.
            
            # Check if the current player has won.
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")  # Show a win message.
                self.reset_game()  # Reset the game after a win.
            # Check if the board is full and no winner (tie).
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")  # Show a tie message.
                self.reset_game()  # Reset the game after a tie.
            else:
                # Switch to the other player.
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Define all possible winning combinations.
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal wins.
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical wins.
                          (0, 4, 8), (2, 4, 6)]  # Diagonal wins.

        # Check if any winning condition is met.
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True  # Return True if there is a winner.
        return False  # Return False if no winner is found.

    def reset_game(self):
        # Reset the game board and UI to the initial state.
        self.board = [""] * 9  # Clear the game board.
        for button in self.buttons:
            button.config(text="")  # Clear the text of all buttons.
        self.current_player = "X"  # Reset the current player to "X".

# Main block to run the game.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window.
    game = TicTacToe(root)  # Instantiate the TicTacToe class.
    root.mainloop()  # Start the Tkinter event loop.
