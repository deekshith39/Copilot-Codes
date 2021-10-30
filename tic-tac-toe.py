# create a tic-tac-toe game
def create_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# function to take player input
def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

# function to place marker on board
def place_marker(board, marker, position):
    board[position[0]][position[1]] = marker

# function to check if board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# print the state of the board after every move with a nice format and a nice border
def print_board(board):
    print("\n")
    print("\t" + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("\t" + "-----------")
    print("\t" + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("\t" + "-----------")
    print("\t" + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("\n")
    

# function to take player input for every move
def player_choice(board):
    position = []
    while position not in range(1, 10):
        position = int(input("Choose a position (1-9): "))
        position = (position-1)//3, (position-1)%3
        if board[position[0]][position[1]] == " ":
            break
        else:
            print("That position is taken. Try again.")
    return position


# function to check if player has won
def win_check(board, mark):
    for row in board:
        if row.count(mark) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

# function to play the game
def play_game():
    board = create_board()
    player1_marker, player2_marker = player_input()
    turn = 0
    while not is_board_full(board):
        if turn == 0:
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            turn += 1
        else:
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            turn -= 1
        print_board(board)
        if win_check(board, player1_marker):
            print("Player 1 wins!")
            break
        elif win_check(board, player2_marker):
            print("Player 2 wins!")
            break
    if not is_board_full(board):
        print("It's a tie!")

# main function
def main():
    play_game()

main()
