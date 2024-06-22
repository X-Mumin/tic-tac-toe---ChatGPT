class Player:
    def __init__(self, mark):
        """Initializes the Player object.

        Args:
            mark (str): The player's mark ('X' or 'O').
        """
        self.mark = mark

    def move(self, game_board, gui, row, col):
        """Handles the player's move.

        Args:
            game_board (list): The 2D list representing the game board.
            gui (TicTacToeGUI): The GUI object to update.
            row (int): The row of the clicked button.
            col (int): The column of the clicked button.
        """
        if game_board[row][col] == "":  # Check if the cell is empty
            game_board[row][col] = self.mark  # Update the game board
            gui.buttons[row][col].config(text=self.mark)  # Update the button text