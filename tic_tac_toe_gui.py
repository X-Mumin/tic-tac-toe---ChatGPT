import tkinter as tk
from tkinter import font

class TicTacToeGUI:
    def __init__(self, master):
        """Initializes the Tic-Tac-Toe GUI."""

        self.master = master
        master.title("Tic-Tac-Toe Almdrasa")

        # Configure font styles
        self.button_font = font.Font(family="Arial", size=24, weight="bold")
        self.label_font = font.Font(family="Arial", size=16)

        # Create a frame to hold the score labels
        score_frame = tk.Frame(master)
        score_frame.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        # Create score labels within the score frame
        self.player_score = tk.StringVar(value="You: 0")
        self.player_score_label = tk.Label(score_frame, textvariable=self.player_score, font=self.label_font)
        self.player_score_label.pack(side="left", padx=10)

        self.computer_score = tk.StringVar(value="Computer: 0")
        self.computer_score_label = tk.Label(score_frame, textvariable=self.computer_score, font=self.label_font)
        self.computer_score_label.pack(side="right", padx=10)

        # Create game message label
        self.game_message = tk.StringVar(value="")
        self.game_message_label = tk.Label(master, textvariable=self.game_message, font=self.label_font)
        self.game_message_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Create a frame to hold the game board buttons
        game_board_frame = tk.Frame(master)
        game_board_frame.grid(row=2, column=0, columnspan=3)

        # Configure grid weights for game board rows and columns
        for i in range(3):
            game_board_frame.rowconfigure(i, weight=1)
            game_board_frame.columnconfigure(i, weight=1)

        # Create game board buttons within the game board frame
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    game_board_frame,  # Place buttons in the game board frame
                    text="",
                    font=self.button_font,
                    width=4,
                    height=2,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j, sticky="nsew")

        # Create restart button
        self.restart_button = tk.Button(master, text="Restart", font=self.label_font, command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def button_click(self, row, col):
        """Handles button clicks on the game board.

        Args:
            row (int): The row of the clicked button.
            col (int): The column of the clicked button.
        """
        # This method will be implemented in the main logic file
        pass

    def restart_game(self):
        """Restarts the game."""
        # This method will be implemented in the main logic file
        pass

# This block is only executed if this script is run directly (not imported)
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()