# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 101
# filename        : gen_0101_gpt4mini_01.py
# timestamp       : 2026-04-06T09:52:41Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 719
# tokens_total    : 1110
# cost_usd        : 0.000490
# --------------------------------------------------------------------
# full_prompt:
#   You are a first-year computer science student completing a programming assignment. Write a complete Python3 implementation of the Connect 4 game with the following requirements:
#   
#   1. Create a 2D board with 7 columns and 6 rows, initialized with spaces
#   2. Support exactly 2 players using checkers "X" and "O"
#   3. Use constant global variables for board dimensions and number of players
#   4. Randomly select which player goes first at the start
#   5. Print the board with column labels A through G before the game starts and after each turn
#   6. Clear the screen before printing using os.system('clear')
#   7. Players input an uppercase letter (A-G) to choose a column
#   8. Validate all input: reject letters outside A-G, reject full columns, reject non-letter input - do NOT end the turn on invalid input, ask again
#   9. Drop the checker to the lowest available row in the chosen column
#   10. After each move, check for a win: 4 in a row horizontally, vertically, or diagonally
#   11. If the board fills with no winner, declare a draw
#   12. When a player wins, print "[Player] won!" and end the game
#   
#   The board must look exactly like this format:
#      A   B   C   D   E   F   G
#   +---+---+---+---+---+---+---+
#   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+
#   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+
#   
#   Provide ONLY the complete Python code. No explanations, no markdown code blocks, just raw Python code starting with import statements.
#   
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column):
    return column in "ABCDEFG"

def get_column_index(column):
    return ord(column) - ord('A')

def is_column_full(board, column):
    return board[0][column] != " "

def drop_checker(board, column, checker):
    for row in reversed(range(ROWS)):
        if board[row][column] == " ":
            board[row][column] = checker
            return True
    return False

def check_winner(board, checker):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if (check_horizontal(board, row, col, checker) or
                check_vertical(board, row, col, checker) or
                check_diagonal(board, row, col, checker)):
                return True
    return False

def check_horizontal(board, row, col, checker):
    if col + 3 < COLUMNS:
        return all(board[row][col + i] == checker for i in range(4))
    return False

def check_vertical(board, row, col, checker):
    if row + 3 < ROWS:
        return all(board[row + i][col] == checker for i in range(4))
    return False

def check_diagonal(board, row, col, checker):
    if row + 3 < ROWS and col + 3 < COLUMNS:
        if all(board[row + i][col + i] == checker for i in range(4)):
            return True
    if row + 3 < ROWS and col - 3 >= 0:
        if all(board[row + i][col - i] == checker for i in range(4)):
            return True
    return False

def is_board_full(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

def main():
    board = create_board()
    current_player = random.choice([PLAYER_X, PLAYER_O])
    
    while True:
        print_board(board)
        column = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        while not is_valid_input(column) or is_column_full(board, get_column_index(column)):
            column = input(f"Invalid input or column full. Player {current_player}, choose again (A-G): ").upper()
        
        drop_checker(board, get_column_index(column), current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    main()