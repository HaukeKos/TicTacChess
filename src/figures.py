# This file is used for handling the figures list of the two players.
# Therefore this class contains two different list of figure, for each player one list

class Figures:

    def __init__(self):
        self.figure_list_blue = ["Rock", "Bishop", "Knight"]
        self.figure_list_red = ["Rock", "Bishop", "Knight"]
        self.move_rock = ((1, 0), (-1, 0), (0, 1), (0, -1))  # ((x-value, y-value), ...)
        self.move_bishop = ((1, 1), (-1, -1), (1, -1), (-1, 1))  # ((x-value, y-value), ...)
        self.move_knight = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))  # ((x-value,
        # y-value), ...)
        self.index = 0

    # Function to get the figure that is currently chosen, depends on the player
    def get_figures(self, player_select, figure):
        if not ((player_select == 1) or (player_select == 2)):
            print("Fehler, Farbe nicht richtig")
        elif player_select == 1:
            # print(self.figure_list_red[self.index])
            return self.figure_list_red[figure]
            # return self.figure_list_red
        elif player_select == 2:
            # print(self.figure_list_red[self.index])
            return self.figure_list_blue[figure]
            # return self.figure_list_blue

    # Function to get the whole figure list with the current figures. This function is used for the buttons in the
    # choosing window
    def get_figures_list(self, player_select):
        if not ((player_select == 1) or (player_select == 2)):
            print("Fehler, Farbe nicht richtig")
        elif player_select == 1:
            return self.figure_list_red
        elif player_select == 2:
            return self.figure_list_blue

    def delete_figures(self, index, player_select):
        if not ((player_select == 1) or (player_select == 2)):
            print("Fehler, Farbe nicht richtig")
        elif player_select == 1:
            self.figure_list_red.remove(self.figure_list_red[index])
        elif player_select == 2:
            self.figure_list_blue.remove(self.figure_list_blue[index])

    # Function to add figures which are stroke back to the list
    def add_figures(self, figure, player_select):
        if not ((player_select == 1) or (player_select == 2)):
            print("Fehler, Farbe nicht richtig")
        elif player_select == 1:
            self.figure_list_red.append(figure)
        elif player_select == 2:
            self.figure_list_blue.append(figure)
