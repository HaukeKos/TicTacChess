# A class that contains the information about the board, on which field which player has which figure
# The syntax, that is used to store the information is:
#       PlayerNumber_Figure

from src.winner_check import winning_check


class FiguresOnBoard:

    def __init__(self):
        self.figures_on_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Board array for the information
        print(self.figures_on_board)

    def add_figure_to_board(self, figure, player, index_board, choose_window, figures, board):
        str_to_save = ""  # String that will be loaded with player and figure information
        # To get the column and row to place the information at the correct element in the array
        column = index_board % 3
        row = int(index_board / 3)
        # Conditions to get the player and the figures
        if not ((player.player_select == 1) or (player.player_select == 2)):
            print("Error in FiguresOnBoard --> add_figures_to_board")
        else:
            # Save player number
            str_to_save = str_to_save + str(player.player_select) + "_"
            # 0 = Rock, 1 = Bishop, 2 = Knight
            if not ((figure == 0) or (figure == 1) or (figure == 2)):
                print("Error in Figures_on_board --> add_figures_to_board")
            # Save player and figure to string
            str_to_save = str_to_save + figures.get_figures(player.player_select, figure)
            # Delete figure from the list
            figures.delete_figures(figure, player.player_select)

        # Add the information to the board-information-array
        self.figures_on_board[row][column] = str_to_save
        # Destroy the window for choosing a figure
        choose_window.destroy()
        # Update board
        board.update_board()
        # Winning check
        if winning_check(self.figures_on_board, player.player_select, board):
            board.display_winner(player.player_select)
        # Change player
        if not board.toggle_var:
            player.change_player()
        # Debug only
        print(self.figures_on_board)

    def add_beatable(self, index_board):
        column = index_board % 3
        row = int(index_board / 3)
        str_strike_save = str(self.figures_on_board[row][column])
        str_strike_save = str_strike_save + "_G"
        self.figures_on_board[row][column] = str_strike_save
        # Debug only
        print(self.figures_on_board)

    def remove_beatable(self):
        for column in range(3):
            for row in range(3):
                str_split = str(self.figures_on_board[row][column]).split("_")
                if len(str_split) == 3:
                    str_split.remove("G")
                if not len(str_split) == 1:
                    self.figures_on_board[row][column] = str_split[0] + "_" + str_split[1]
