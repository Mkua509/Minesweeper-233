import pytest
from functions_minesweeper import *

def test_count_adjacent_mines_in_corner():
    board = [
        'X', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O']
    count = count_adjacent_mines(board, 0, 4)
    assert count == 0

# Insert mines test
def test_insert_mines():
    board = initialise_board()
    positions = [[1, 1], [2, 2]]
    insert_mines(board, positions)
    # Changes to 1D so testing the 1D string
    assert board[6] == "X"  
    assert board[12] == "X" 

# Testing for count adjacent in the center
def test_count_adjacent_mines_center():
    board = [
        'O', 'O', 'O', 'O', 'O',
        'O', 'X', 'O', 'X', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O']
    count = count_adjacent_mines(board, 2, 2)  
    assert count == 2

# Test for play turn where all mines except center
def test_play_turn_all_mines():
    board = ['X', 'X', 'X', 'X', 'X',
             'X', 'X', 'X', 'X', 'X',
             'X', 'X', 'O', 'X', 'X',
             'X', 'X', 'X', 'X', 'X',
             'X', 'X', 'X', 'X', 'X']
    
    updated_board, hit_mine = play_turn(board, 2, 2) 
    # 8 Mines around
    assert updated_board[12] == '8'
    # Since no mine was hit, hit_mine should be False
    assert hit_mine is False

def test_play_mine_hit():
    board = ['X', 'X', 'X', 'X', 'X',
             'X', 'X', 'X', 'X', 'X',
             'X', 'X', 'O', 'X', 'X',
             'X', 'X', 'X', 'X', 'X',
             'X', 'X', 'X', 'X', 'X']
    
    updated_board, hit_mine = play_turn(board, 2, 3) 
    # Since a mine was hit True
    assert hit_mine is True


# Test for check_win

def test_check_win():
    # Board where everything is space
    board = [' ']*25
    # The game should be true and won
    result = check_win(board)
    assert result is True

    # Board where not all is space
    board[10] = 'O'
    # The game should be false and not won
    result = check_win(board)
    assert result is False
