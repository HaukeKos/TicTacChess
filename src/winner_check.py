# This function is used to check, if a player has won the game

def winning_check(figures_on_board, player_select, board):
    win = None
    fields = 3
    if not ((player_select == 1) or (player_select == 2)):
        print("Errors in winning_check")
    else:
        player = str(player_select)
        # Check the row
        for i in range(fields):
            win = True
            for j in range(fields):
                if not str(figures_on_board[i][j]).startswith(player):
                    win = False
                    break
            if win:
                board.display_winner(player_select)

        # Check the column
        for i in range(fields):
            win = True
            for j in range(fields):
                if not str(figures_on_board[j][i]).startswith(player):
                    win = False
                    break
            if win:
                board.display_winner(player_select)

        # Check the diagonals
        win = True
        for i in range(fields):
            if not str(figures_on_board[i][i]).startswith(player):
                win = False
                break
        if win:
            board.display_winner(player_select)

        win = True
        for i in range(fields):
            if not str(figures_on_board[i][fields - 1 - i]).startswith(player):
                win = False
                break
        if win:
            board.display_winner(player_select)
