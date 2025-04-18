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
            # 2D to 3D
            i = row * 5 + col
            # fill in board string
            board = board + new_board[i] + " "
        board = board + "\n"
    print (board)

'''
Task 3: Inserting the mines
A function called insert_mines that inserts mines to the board at specified postions.
The mines should be represented by the X character
Input 1: a list representing the board
Input 2: list of lists representing each mine location. The first index in each nested list represents the row (0-4) and the second index represents the
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
# my_board = initialise_board() 
# insert_mine(my_board, [[1, 2], [3, 4], [0, 0]]) 
# display_board(my_board)  # It prints the board inside

'''
Task 4: Counting Adjacent Mines
A function count_adjacent_mines that counts the number of mines, X, adjacent (including diagonals!) to the selected row, col position
Input 1: a list representing the board
Input 2: an int reprersenting the row (0-4) of the square being checked for adjacent mines
Input 3: an int representing the col (0-4) of the square being checked for adjacent mines
Output: int representing the number (0-8) of adjacent mines
Author: Maternus Kuang
'''

def count_adjacent_mines(board, rows, cols):
    count = 0

# loop through rows around cell
    for r in range(rows - 1, rows + 2):
        # loop thorugh cols around cell
        for c in range(cols - 1, cols + 2):
            # skip picked cell
            if r == rows and c == cols:
                continue

            # withen boundarys
            if 0 <= r < 5 and 0 <= c < 5:
                index = r * 5 + c
                if board[index] == "X":
                    count += 1

    return count

board = initialise_board()
insert_mine(board, [[0, 0], [1, 1], [2, 2]])
display_board(board)
print(count_adjacent_mines(board, 3, 2))  