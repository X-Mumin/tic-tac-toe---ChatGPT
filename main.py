import tkinter as tk
from tic_tac_toe_gui import TicTacToeGUI
from Player import Player
from Computer import Computer

class TicTacToeGame:
    def __init__(self, master):
        """Initializes the Tic-Tac-Toe game."""

        self.master = master
        self.gui = TicTacToeGUI(master)
        self.game_board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.player = Player("X")
        self.computer = Computer("O")
        self.current_player = self.player  # Start with the player
        self.game_over = False  # Flag to indicate if the game is over

        # Initialize scores
        self.player_score = 0
        self.computer_score = 0
        self.update_score_labels() # Update the score labels initially

        # Connect button clicks to the game logic
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))

        # Connect the restart button to the restart_game method
        self.gui.restart_button.config(command=self.restart_game)
        self.restart_game()  # Initialize the board here

    def button_click(self, row, col):
        """Handles button clicks on the game board."""

        if self.game_board[row][col] == "" and not self.game_over:
            if self.current_player == self.player:
                self.current_player.move(self.game_board, self.gui, row, col)  # Player move
                self.switch_player()  # Switch to computer

                # Computer's turn immediately after player's move
                if self.current_player == self.computer and not self.game_over:
                    self.computer.move(self.game_board, self.gui)  # Computer move
                    self.switch_player()  # Switch back to player

            self.check_for_winner()  # Call the function to check for a winner!
            
    def switch_player(self):
        """Switches the current player."""
        self.current_player = self.computer if self.current_player == self.player else self.player 

    def check_for_winner(self):
        """Checks for a winner or a draw."""

        # --- Winning Patterns (for coloring) ---
        winning_patterns = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
        ]

        # Check for a winner and get the winning pattern
        for pattern in winning_patterns:
            a, b, c = pattern[0], pattern[1], pattern[2]
            if self.game_board[a[0]][a[1]] == self.game_board[b[0]][b[1]] == self.game_board[c[0]][c[1]] and self.game_board[a[0]][a[1]] != "":
                self.declare_winner(self.game_board[a[0]][a[1]], pattern)  # Pass the pattern to declare_winner
                return

        # Check for a draw
        if all(cell != "" for row in self.game_board for cell in row):
            self.declare_winner("Tie", None)  # No winning pattern for a tie

    def declare_winner(self, winner, winning_pattern):
        """Declares the winner, updates the game state, and colors the board."""

        self.game_over = True
        if winner == "Tie":
            self.gui.game_message.set("It's a tie!")
            # Color the entire board red for a tie
            for i in range(3):
                for j in range(3):
                    self.gui.buttons[i][j].config(bg="red")
        else:
            self.gui.game_message.set(f"{winner} wins!")
            if winner == "X":
                self.player_score += 1
            else:
                self.computer_score += 1

            # Color the winning sequence
            if winning_pattern:
                for row, col in winning_pattern:
                    self.gui.buttons[row][col].config(bg="cyan")  # Change button background to cyan

        self.update_score_labels()

    def update_score_labels(self):
        """Updates the score labels in the GUI."""

        self.gui.player_score.set(f"You: {self.player_score}")
        self.gui.computer_score.set(f"Computer: {self.computer_score}")

    def restart_game(self):
        """Restarts the game."""

        self.game_board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.current_player = self.player
        self.game_over = False
        self.gui.game_message.set("")  # Clear the game message

        # Reset the button texts and colors in the GUI
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(text="", bg="SystemButtonFace")  # Reset to default color

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()