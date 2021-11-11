# This class contains the functions to alternate the players and teh color check, to display the winner in the color of
# their player color
class Player:

    def __init__(self):
        self.player_select = 1  # Red = 1, Blue = 2

    def color_check(self):
        if not ((self.player_select == 1) or (self.player_select == 2)):
            print("Fehler, falsche Anzahl an Spielern")
        elif self.player_select == 1:
            return "Red"
        elif self.player_select == 2:
            return "Blue"

    def change_player(self):
        if not ((self.player_select == 1) or (self.player_select == 2)):
            print("Fehler, falsche Anzahl an Spielern")
        elif self.player_select == 1:
            self.player_select = 2
        elif self.player_select == 2:
            self.player_select = 1
