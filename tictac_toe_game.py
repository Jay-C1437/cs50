import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        # self.root.geometry("100x500")
        self.root.resizable(False, False)
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
    class TicTacToe:
        def __init__(self, root):
            # Initialize the main window and game variables
            self.root = root
            self.root.title("Tic Tac Toe")
            # self.root.geometry("400x400")
            self.root.resizable(False, False)
            self.current_player = "X"  # Start with player "X"
            self.board = [""] * 9  # Initialize the game board
            self.buttons = []  # List to hold button widgets
            self.create_widgets()  # Create the game buttons

        def create_widgets(self):
            # Create 9 buttons for the Tic Tac Toe grid
            for i in range(9):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda i=i: self.on_button_click(i))
                button.grid(row=i//3, column=i%3)  # Arrange buttons in a 3x3 grid
                self.buttons.append(button)  # Add button to the list

        def on_button_click(self, index):
            # Handle button click event
            if self.board[index] == "":
                self.board[index] = self.current_player  # Update the board
                self.buttons[index].config(text=self.current_player)  # Update button text
                if self.check_winner():
                    messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                    self.reset_game()  # Reset the game if there's a winner
                elif "" not in self.board:
                    messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                    self.reset_game()  # Reset the game if it's a tie
                else:
                    # Switch player
                    self.current_player = "O" if self.current_player == "X" else "X"

        def check_winner(self):
            # Check if there's a winner
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                              (0, 3, 6), (1, 4, 7), (2, 5, 8),
                              (0, 4, 8), (2, 4, 6)]
            for condition in win_conditions:
                if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                    return True
            return False

        def reset_game(self):
            # Reset the game to the initial state
            self.board = [""] * 9
            for button in self.buttons:
                button.config(text="")
            self.current_player = "X"  # Start with player "X"

    if __name__ == "__main__":
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()