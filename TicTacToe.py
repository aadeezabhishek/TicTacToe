board=["-","-","-",
       "-","-","-",
       "-","-","-"]

game_still_going = True
winner = None
current_player = "X"

def display_board():
    print("|"+board[0] + "|"+board[1] + "|"+board[2] + "|")
    print("|"+board[3] + "|"+board[4] + "|"+board[5] + "|")
    print("|"+board[6] + "|"+board[7] + "|"+board[8] + "|")

def play_game():

    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner=="X" or winner=="O":
            print(winner +"'s won")
    elif winner == None:
            print("Tie")


def handle_turn(player):
    print(player+"'s turn")
    position=input("Enter any number from 1 to 9\t")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position =input("Invalid Input! Choose number from 1 to 9\t")

        position = int(position)-1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there; Go again!\t")


    board[position]=player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2]!="-"
    row2 = board[3] == board[4] == board[5]!="-"
    row3 = board[6] == board[7] == board[8] !="-"

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[7]
    return

def check_column():
    global game_still_going
    col1 = board[0] == board[3] == board[6]!="-"
    col2 = board[1] == board[4] == board[7]!="-"
    col3 = board[2] == board[5] == board[8] !="-"

    if col1 or col3 or col2:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_diagonal():
    global game_still_going
    dgn1 = board[0] == board[4] == board[8]!="-"
    dgn2 = board[2] == board[4] == board[6]!="-"

    if dgn1 or dgn2:
        game_still_going = False
        return board[4]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()