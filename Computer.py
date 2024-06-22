import random

class Computer:
    def __init__(self, mark):
        """Initializes the Computer object.

        Args:
            mark (str): The computer's mark ('X' or 'O').
        """
        self.mark = mark

    def move(self, game_board, gui):
        """Handles the computer's move.

        Args:
            game_board (list): The 2D list representing the game board.
            gui (TicTacToeGUI): The GUI object to update.
        """
        empty_cells = [(row, col) for row in range(3) for col in range(3) if game_board[row][col] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            game_board[row][col] = self.mark  # Update the game board
            gui.buttons[row][col].config(text=self.mark)  # Update the button text