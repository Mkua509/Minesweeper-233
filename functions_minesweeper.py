'''
Task 1: Initialising the Board
A function called initialise_board that initialises the Minesweeper grid

Arguments:

Returns:
list: It containing 25 items, each item being the string O, and each representing a square not selected

Notes: 
The baord is 1D representing 5x5 grid
All squares are "O" at first

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

Arguments:
new_board(list): list representing the board

Returns:

Notes:
Hiddent mines "X" are displayed as "O"
All other values are shown normally

Author: Maternus Kuang
'''


def display_board(new_board):
    # intialise string for board
    board = "" 
    # loop through rows and cols 5x5
    for row in range(5):
        for col in range(5):
            # 2D to 1D
            i = row * 5 + col
            # If the square a mine display as "O"
            if new_board[i] == "X":
                board = board + "O "
            # Otherwise fill in board string 
            else:
                board = board + new_board[i] + " "
        board = board + "\n"
    print (board)


'''
Task 3: Inserting the mines
A function called insert_mines that inserts mines to the board at specified postions.
The mines should be represented by the X character

Arguments:
board(list): a list representing the board
positions(list of a list): list of lists representing each mine location. The first index in each nested list represents the row (0-4) and the second index represents the column (0-4)

Returns:

Notes:
Modifies the inputted board and inputs X in locations inputted

Author: Maternus Kuang
'''

def insert_mines(board, positions):
    # loop through given list
    for n in positions:
        # access row and col of specfied positions
        row = n[0]
        col = n[1]
        # 2D to 1D
        i = row * 5 + col  
        # place mine at given location
        board[i] = "X"  


'''
Task 4: Counting Adjacent Mines
A function count_adjacent_mines that counts the number of mines, X, adjacent (including diagonals!) to the selected row, col position

Arguments:
board(list): a list representing the board
rows(int): an int reprersenting the row (0-4) of the square being checked for adjacent mines
cols(int): an int representing the col (0-4) of the square being checked for adjacent mines

Returns:
int: int representing the number (0-8) of adjacent mines

Notes:
Skips the square chosen
Checks if the surrounding are withen boundary (not outside)

Author: Maternus Kuang
'''

def count_adjacent_mines(board, rows, cols):
    count = 0

# loop through rows around cell
    for r in range(rows - 1, rows + 2):
        # loop thorugh cols around cell
        for c in range(cols - 1, cols + 2):
            # skip the picked cell
            if r == rows and c == cols:
                continue

            # withan boundarys
            if 0 <= r< 5 and 0 <= c < 5:
                i = r * 5 + c
                if board[i] == "X":
                    count += 1

    return count


'''
Task 5: Playing a Turn
A function play_turn that plays a turn using the provided row and col on the provided board. If a hidden mine is selcted, it should change to a # character. 
Otherwise the number of mines adjacent to the selected postion should replace the exisitng charcter. If none are adjacent mines, the space character should be used

Arguments:
board(list): a list representing the board
rows(int): an int reprersenting the row (0-4) of postion being selected 
cols(int): an int representing the col (0-4) of postion being selected

Returns:
list: a list representing the updated board. returning the updated board (unlike func 3)
boolean: bool flagging of a mine was selected True if a mine was selected, False otherwise)

Notes:
Square changes to "#" if mine is selected
Change to space " " if no adjacent numbers
Else the square shows the count

Author: Maternus Kuang
'''
    
def play_turn (board, rows, cols):
    # Turn 2d into 1d
    i = rows * 5 + cols

    # If selected mine
    if board[i] == "X":
        board[i] = "#"
        return board, True
    else:
        # If no adjacent mines replace with space
        count = count_adjacent_mines(board, rows, cols)
        if count == 0:
            board[i] = " "
        # Otherwise replace with number counted
        else:
            board[i] = str(count)
        return board, False
    
'''
Task 6: Checking for a Win!
A function check_win that determines if the playter has won the game. This occurs when all positions that do not contain a mine have been selected.

Arguments:
board(list): a list representing the board

Returns:
boolean: a bool representing if the game has been won (True) or not (False)

Notes:
The game over and won if no more "O" left 

Author: Maternus Kuang
'''

def check_win(board): 
    # Loop through the entire list if there is a O they have not won 
    for n in board:
        if n == "O":
            return False
    # Otherwise return true
    return True

'''
Task 7: Play a Game
A function play_game that can play minesweeper game from start to finish

Arguments:
positions(list of lists): a list of lists indicating the positions that mines will be placed in the board

Returns:

Notes:
Continues until the player hits a mine or wins
Take the user inputs for rows and cols during the game in format EX: 1 1

Author: Maternus Kuang
'''

def play_game(positions):
    board = initialise_board()
    insert_mines(board, positions)
    display_board(board)
    game_over = False
    
    while not game_over:
        user_input = input("Enter row and col seperated by a space (ex: 1 3):")

        split = user_input.split()
        row = int(split[0])
        col = int(split[1])

        board, hit_mine = play_turn(board, row, col)

        display_board(board)

        if hit_mine:

            print("You hit a mine, Game over.")
            game_over = True
        elif check_win(board):
            print("You won!")