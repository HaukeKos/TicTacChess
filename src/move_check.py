# This function is used to check which fields are possible to move for the selected figure

def check_move(board, player_select, index_current_button, move_set, column, row, figures_on_board, Figures_on_Board):
    if not ((player_select == 1) or (player_select == 2)):
        print("Errors in move_Check")
    else:
        # Next row and column with the step of the move set
        column_next = column + move_set[0]
        row_next = row + move_set[1]
        # New index with the new row and column
        index_next_button = column_next + 3 * row_next  # 3 = width
        # Check if the new column and row is on the board
        if 0 <= column_next < 3 and 0 <= row_next < 3:
            # Check if the button on the board is a figure of the other player or empty
            if not str(figures_on_board[row_next][column_next]).startswith(str(player_select)):
                # Buttons where the player can move to printed with a green background
                Figures_on_Board.add_beatable(index_next_button)
                # Check if there is a empty field and the figure is not a knight to check if the field behind that is
                # also able to move on
                if not board.buttons[index_current_button]["text"] == "Knight" and \
                        figures_on_board[row_next][column_next] == 0:
                    # Update column and row to the field behind the current checked field
                    column = column + move_set[0]
                    row = row + move_set[1]
                    check_move(board, player_select, index_current_button, move_set, column, row, figures_on_board)
