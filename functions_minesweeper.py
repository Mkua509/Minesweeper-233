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
    return board

'''
Task 3: Inserting the mines
A function called insert_mines that inserts mines to the board at specified postions.
The mines should be represented by the X character
Input 1: a list representing the board
Input 2:list of lists representing each mine location. The first index in
each nested list represents the row (0-4) and the second index represents the
column (0-4)
Output: No output
Author: Maternus Kuang
'''

def insert_mine(board, positions):
    # loop through given list
    for n in positions:
        # access row and col of specfied positions
        row = n[0]
        col = n[1]
        # 2D to 1D
        i = row * 5 + col  
        # place mine at given location
        board[i] = "X"  

# example usage
my_board = initialise_board() 
insert_mine(my_board, [[1, 2], [3, 4], [0, 0]]) 
board_string = display_board(my_board)  
print(board_string) 
