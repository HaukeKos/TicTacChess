import time
import tkinter as tk
from tkinter import Toplevel

from src.figures import Figures
from src.move_check import check_move
from src.player import Player
from src.winner_check import winning_check
from src.figuresonboard import FiguresOnBoard


class Board(tk.Tk):
    tk.height = 900
    tk.width = 900
    tk.frame_size = str(tk.width) + "x" + str(tk.height)

    def __init__(self):
        super().__init__()
        self.geometry(tk.frame_size)
        self.title("Tic Tac Chess")

        self.buttons = []
        self.frames_list = []
        self.figures = Figures()
        self.figures_on_board = FiguresOnBoard()
        self.player = Player()
        self.set_round = 1
        self.game_phase = 1  # First = 1, Second = 2
        self.old_index = None
        self.attack_figure = ""
        self.toggle_var = False

        self.create_buttons()

    # Function to create the 9 buttons on the game board
    def create_buttons(self):
        # Index for iterating through all fields on the board
        index = 0
        for i in range(3):
            for j in range(3):
                # Frames are used, because with them it is possible to assign the buttons a width and height in pixel
                # size
                self.frames_list.append(tk.Frame(self, height=tk.height / 3, width=tk.width / 3))
                self.frames_list[index].propagate(False)
                self.frames_list[index].grid(row=i, column=j)
                # Lambda function is used to pass the index as argument
                # self.buttons.append(tk.Button(self.frames_list[index],
                # command=lambda index=index: self.choose_game_phase(index)))
                self.buttons.append(tk.Button(self.frames_list[index],
                                              command=lambda index=index: self.open_choose_window(index)))
                self.buttons[index].pack(fill=tk.BOTH, expand=True)
                index += 1

    def open_choose_window(self, index_board):
        # If no figures left and no winner, then go to the striking game phase
        if (len(self.figures.get_figures_list(1)) == 0) and (len(self.figures.get_figures_list(2)) == 0):
            self.choose_figure_to_move(index_board)
        else:
            # Variables
            frames_list_top_level = []
            buttons_top_level = []
            figures_len = 3

            # Open TopLevel
            choose_window = Toplevel()
            choose_window.height = 100
            choose_window.width = 300
            choose_window.frame_size = str(choose_window.width) + "x" + str(choose_window.height)
            choose_window.geometry(choose_window.frame_size)
            choose_window.title("Choose Figure")

            # Get the length of the remaining figures of the player
            if not ((self.player.player_select == 1) or (self.player.player_select == 2)):
                print("Fehler, Farbe nicht richtig")
            elif self.player.player_select == 1:
                figures_len = len(self.figures.figure_list_red)
            elif self.player.player_select == 2:
                figures_len = len(self.figures.figure_list_blue)

            # Get the list of remaining figures
            figure_list = self.figures.get_figures_list(self.player.player_select)

            # Build Buttons
            for i in range(figures_len):
                # Frames are used, because with them it is possible to assign the buttons a width and height in pixel
                # size
                frames_list_top_level.append(tk.Frame(choose_window, height=choose_window.height,
                                                      width=choose_window.width / figures_len))
                frames_list_top_level[i].propagate(False)
                frames_list_top_level[i].grid(row=0, column=i)
                # Lambda function is used to pass the index from the board and figure and the window for choosing the
                # figure as argument
                buttons_top_level.append(tk.Button(frames_list_top_level[i], text=figure_list[i],
                                                   command=lambda index_figure=i:
                                                   self.figures_on_board.add_figure_to_board(
                                                       index_figure, self.player, index_board, choose_window,
                                                       self.figures, self)))
                buttons_top_level[i].pack(fill=tk.BOTH, expand=True)
            choose_window.mainloop()

    def update_board(self):
        # For all buttons on board
        for index in range(9):
            # Change index into column and row
            column = index % 3
            row = int(index / 3)
            # Split the string into player and figure
            # Syntax: [Player, Figure]
            str_arr = str(self.figures_on_board.figures_on_board[row][column]).split("_")
            # Check if there is a figure
            if not str_arr[-1] == "0":
                # Print figure on the button
                self.buttons[index].configure(text=str_arr[1])
                # Print the right color of text, depends on the player
                if str_arr[0] == "1":
                    self.buttons[index].configure(fg="Red")
                else:
                    self.buttons[index].configure(fg="Blue")
                # Print all white for the purpose of painting teh fields white if a strike move was done
                self.buttons[index].configure(bg="White")
                # Paint beatable figures green
                if len(str_arr) == 3:
                    self.buttons[index].configure(bg="Green")
            else:
                self.buttons[index].configure(text="")
        self.update()

    # Function to choose the move and get the move set of the chosen figure
    def choose_figure_to_move(self, index_board):
        # Transfer the 1D index to a 2D index with row and column
        column = index_board % 3  # x-value
        row = int(index_board / 3)  # y-value
        # Figure out which figure move set needs to be used
        print(self.figures_on_board.figures_on_board[row][column])
        if str(self.figures_on_board.figures_on_board[row][column]).endswith("Rock"):
            move_set = self.figures.move_rock
        elif str(self.figures_on_board.figures_on_board[row][column]).endswith("Bishop"):
            move_set = self.figures.move_bishop
        else:
            move_set = self.figures.move_knight
        # Check every field in range of the move set
        for move in move_set:
            check_move(self, self.player.player_select, index_board, move, column, row,
                       self.figures_on_board.figures_on_board, self.figures_on_board)

        self.update_board()
        time.sleep(1)
        self.wait_for_legal_input(index_board)

    def wait_for_legal_input(self, index_board):
        # Change the command of the button when is clicked
        for index in range(9):
            self.buttons[index].configure(command=lambda i=index: self.strike_move(i, index_board))

    def change_to_open_choose_window(self):
        for index in range(9):
            self.buttons[index].configure(command=lambda i=index: self.open_choose_window(i))

    def strike_move(self, index_strike_figure, index_board):
        print(index_strike_figure)
        self.toggle_var = True
        # If not the beatable button is clicked
        if not self.buttons[index_strike_figure]["bg"] == "Green":
            self.wait_for_legal_input(index_board)
        else:
            # Get the figure who is beat to add it to the list of figures for the beat player
            strike_column = index_strike_figure % 3  # x-value
            strike_row = int(index_strike_figure / 3)  # y-value
            column = index_board % 3  # x-value
            row = int(index_board / 3)  # y-value
            # Change player to get the figure to the right player back
            self.player.change_player()
            print("Player")
            print(self.player.player_select)
            # Get the figure who was beat and added to the beat players list
            str_split = str(self.figures_on_board.figures_on_board[strike_row][strike_column]).split("_")
            self.figures.add_figures(str_split[1], self.player.player_select)
            # Get the figure who stroke and placed it on the stroke field
            self.figures_on_board.figures_on_board[strike_row][strike_column] = \
                self.figures_on_board.figures_on_board[row][column]
            # Remove figure from the list of figures on board
            self.figures_on_board.figures_on_board[row][column] = "0"
            # self.buttons[index_strike_figure].configure(bg="White")
            self.figures_on_board.remove_beatable()
            print(self.figures_on_board.figures_on_board)
            self.update_board()
            self.change_to_open_choose_window()

    # Function to display the winner
    def display_winner(self, player_select):
        winner_window = Toplevel()
        winner_window.title("Winner")
        winner_str = "Player " + str(player_select) + " has won the game!"
        winner_label = tk.Label(winner_window, text=winner_str, font=("Arial", 28), fg=self.player.color_check())
        winner_label.grid(row=0, column=0)
        winner_window.mainloop()
