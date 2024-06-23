import tkinter as tk
from tic_tac_toe_gui import TicTacToeGUI
from Player import Player
from Computer import Computer

class TicTacToeGame:
    """
    Represents a Tic-Tac-Toe game with a GUI, handling game logic, player turns,
    and win/draw conditions.
    """
    def __init__(self, master):
        """
        Initializes the Tic-Tac-Toe game.

        Args:
            master: The parent Tkinter window.
        """
        self.master = master
        self.gui = TicTacToeGUI(master)
        self.restart_game()  # Initialize the board here
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0

    def _create_game_elements(self):
        """
        Creates and initializes game elements like the board and players.

        This method sets up the game board, creates player and computer objects,
        sets the starting player, initializes the game state, and resets scores.
        """
        self.game_board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.player = Player("X")
        self.computer = Computer("O")
        self.current_player = self.player  # Start with the player
        self.game_over = False  # Flag to indicate if the game is over


    def _setup_gui_callbacks(self):
        """
        Connects button clicks to game logic.

        This method associates each button in the GUI grid with the 
        button_click method, enabling the game to respond to player input.
        It also connects the restart button to the restart_game method.
        """
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))

        # Connect the restart button to the restart_game method
        self.gui.restart_button.config(command=self.restart_game)

    def button_click(self, row, col):
        """
        Handles button clicks on the game board.

        If the clicked cell is empty and the game is not over, it allows
        the current player to make a move. Then, it switches to the next
        player and checks for a winner or a draw.

        Args:
            row: The row of the clicked button.
            col: The column of the clicked button.
        """
        if self.game_board[row][col] == "" and not self.game_over:
            if self.current_player == self.player:
                self.current_player.move(self.game_board, self.gui, row, col)  # Player move
                self.switch_player()  # Switch to computer
                self.check_for_winner()  # Call the function to check for a winner!

                # Computer's turn immediately after player's move
                if self.current_player == self.computer and not self.game_over:
                    self.computer.move(self.game_board, self.gui)  # Computer move
                    self.switch_player()  # Switch back to player
                    self.check_for_winner()  # Call the function to check for a winner!


    def switch_player(self):
        """
        Switches the current player from player to computer or vice versa.
        """
        self.current_player = self.computer if self.current_player == self.player else self.player 

    def _check_winning_pattern(self):
        """
        Checks for a winner and returns the winner and winning pattern (if any).

        This method iterates through all possible winning patterns on the game
        board. If a player's marks (X or O) form a winning pattern, the method
        returns the winner and the winning pattern. Otherwise, it checks for a tie.
        If neither a win nor a tie is found, it returns None.

        Returns:
            A tuple containing:
                - The winner (either "X", "O", or "Tie"), or None if no winner yet.
                - The winning pattern (a list of cell coordinates), or None if no winner or a tie.
        """
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

        for pattern in winning_patterns:
            a, b, c = pattern[0], pattern[1], pattern[2]
            if self.game_board[a[0]][a[1]] == self.game_board[b[0]][b[1]] == self.game_board[c[0]][c[1]] and self.game_board[a[0]][a[1]] != "":
                return self.game_board[a[0]][a[1]], pattern  # Winner, Winning Pattern

        if all(cell != "" for row in self.game_board for cell in row):
            return "Tie", None  # It's a tie
        
        return None, None  # No winner yet

    def check_for_winner(self):
        """
        Checks for a winner or a draw and updates the game state.

        This method calls _check_winning_pattern to determine if there's a winner.
        If a winner or a tie is found, it calls declare_winner to handle the game outcome.
        """
        winner, winning_pattern = self._check_winning_pattern()
        if winner:
            self.declare_winner(winner, winning_pattern)

    def declare_winner(self, winner, winning_pattern):
        """
        Declares the winner, updates the game state, and colors the board.

        If the game ends in a tie, it colors the board red. If there's a winner,
        it colors the winning sequence cyan, updates the scores, and displays
        the winner.

        Args:
            winner: The winner of the game ("X", "O", or "Tie").
            winning_pattern: The winning pattern (a list of cell coordinates).
        """
        self.game_over = True
        if winner == "Tie":
            self.gui.game_message.set("It's a tie!")
            self._color_board(color="red") # Color the entire board red for a tie
        else:
            self.gui.game_message.set(f"{winner} wins!")
            if winner == "X":
                self.player_score += 1
            else:
                self.computer_score += 1
            self._color_winning_sequence(winning_pattern)
        self.update_score_labels()

    def _color_board(self, color):
        """
        Colors the entire game board with the specified color.

        Args:
            color: The color to set the background of all cells.
        """
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(bg=color)

    def _color_winning_sequence(self, winning_pattern):
        """
        Colors the winning sequence on the board.

        Args:
            winning_pattern: The winning pattern (a list of cell coordinates).
        """
        if winning_pattern:
            for row, col in winning_pattern:
                self.gui.buttons[row][col].config(bg="cyan")

    def update_score_labels(self):
        """Updates the score labels in the GUI."""
        self.gui.player_score.set(f"You: {self.player_score}")
        self.gui.computer_score.set(f"Computer: {self.computer_score}")

    def restart_game(self):
        """
        Restarts the game to its initial state.

        This method resets the game board, player turns, clears the game message,
        resets button colors, and updates the score labels.
        """
        self._create_game_elements()
        self._setup_gui_callbacks()
        # self.update_score_labels()
        self.gui.game_message.set("")  # Clear the game message
        
        # Reset the button texts and colors in the GUI
        for i in range(3):
            for j in range(3):
                self.gui.buttons[i][j].config(text="", bg="SystemButtonFace") 

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()