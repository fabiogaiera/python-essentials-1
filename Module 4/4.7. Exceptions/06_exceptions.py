# LAB
from random import randrange

board_list = []
dict_positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}


# The function accepts one parameter containing the board's current status
# and prints it out to the console.
def display_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()


# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.
def enter_move(board):
    while True:
        try:
            position = int(input("Insert move: "))
            tup = dict_positions.get(position)
            if tup in make_list_of_free_fields(board):
                board[tup[0]][tup[1]] = 'O'
                print("Human move")
                display_board(board)
                return board
        except TypeError:
            print("Not correct move")


# The function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers.
def make_list_of_free_fields(board):
    lst = []
    k = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == k:
                lst.append((i, j))
            k += 1
    return lst


# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    if sign == board[0][0] and sign == board[0][1] and sign == board[0][2]:
        return True
    elif sign == board[1][0] and sign == board[1][1] and sign == board[1][2]:
        return True
    elif sign == board[2][0] and sign == board[2][1] and sign == board[2][2]:
        return True
    elif sign == board[0][0] and sign == board[1][0] and sign == board[2][0]:
        return True
    elif sign == board[0][1] and sign == board[1][1] and sign == board[2][1]:
        return True
    elif sign == board[0][2] and sign == board[1][2] and sign == board[2][2]:
        return True
    elif sign == board[0][0] and sign == board[1][1] and sign == board[2][2]:
        return True
    elif sign == board[0][2] and sign == board[1][1] and sign == board[2][0]:
        return True
    else:
        return False


# The function draws the computer's move and updates the board.
def draw_move(board):
    while True:
        free_lst = make_list_of_free_fields(board)
        position = randrange(8)
        tup = dict_positions.get(position)
        if tup in free_lst:
            board[tup[0]][tup[1]] = 'X'
            print("Computer move")
            display_board(board)
            return board


def initialize_board(board):
    board = [[] for i in range(3)]
    k = 1
    for i in range(3):
        for j in range(3):
            board[i].append(k)
            k += 1
    return board


def initialize_game(board):
    board[1][1] = 'X'
    print("Computer move")
    display_board(board_list)
    return board


board_list = initialize_board(board_list)
board_list = initialize_game(board_list)

victory = False
free_fields = make_list_of_free_fields(board_list)

while True and len(free_fields) != 0:

    board_list = enter_move(board_list)
    victory_human = victory_for(board_list, 'O')
    if victory_human:
        print("Human won")
        break

    board_list = draw_move(board_list)
    victory_computer = victory_for(board_list, 'X')
    if victory_computer:
        print("Computer won")
        break

    free_fields = make_list_of_free_fields(board_list)
