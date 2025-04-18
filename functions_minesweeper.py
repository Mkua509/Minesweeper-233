'''
Task 1: Initialising the Board
A function called initialise_board that initialises the Minesweeper grid
Input: none
Output: a list representing the Minesweeper board. 
It containing 25 items, each item being the string O, and each representing a square not selected
Author: Maternus Kuang
'''

def initialise_board():
    # list representing the minesweeper board
    initialise = ["O"] * 25
    
    # return list
    return initialise

'''
Task 2: Visualizing the Board
A function called display_board that displays screen 5*5 minesweeper board. 0s, spaces and num of adjacent mines
are displayed. However hidden mines, X are displayed as 0.
Input: list representing the board
Output: none
Author: Maternus Kuang
'''


def display_board(new_board):
    # intialise string for board
    board = "" 
    # loop through rows and cols 5x5
    for row in range(5):
        for col in range(5):
            # index for rows 
            i = row * 5 + col
            # fill in board string
            board = board + new_board[i] + " "
        board = board + "\n"
    print(board)




# test the board display
my_board = initialise_board()
display_board(my_board)