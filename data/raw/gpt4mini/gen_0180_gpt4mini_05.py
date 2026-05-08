# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 180
# filename        : gen_0180_gpt4mini_05.py
# timestamp       : 2026-04-06T09:23:07Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 784
# tokens_total    : 1171
# cost_usd        : 0.000528
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
#   Write with descriptive function names and minimal comments.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY_SPACE = ' '
PLAYER_ONE = 'X'
PLAYER_TWO = 'O'

def create_board():
    return [[EMPTY_SPACE for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column):
    return column in 'ABCDEFG' and column_to_index(column) is not None

def column_to_index(column):
    return ord(column) - ord('A')

def is_column_full(board, col_index):
    return board[0][col_index] != EMPTY_SPACE

def drop_checker(board, col_index, checker):
    for row in reversed(board):
        if row[col_index] == EMPTY_SPACE:
            row[col_index] = checker
            return True
    return False

def check_winner(board, checker):
    return (check_horizontal(board, checker) or 
            check_vertical(board, checker) or 
            check_diagonal(board, checker))

def check_horizontal(board, checker):
    for row in board:
        count = 0
        for cell in row:
            count = count + 1 if cell == checker else 0
            if count == 4:
                return True
    return False

def check_vertical(board, checker):
    for col in range(COLS):
        count = 0
        for row in range(ROWS):
            count = count + 1 if board[row][col] == checker else 0
            if count == 4:
                return True
    return False

def check_diagonal(board, checker):
    for row in range(ROWS):
        for col in range(COLS):
            if (col + 3 < COLS and row + 3 < ROWS and
                all(board[row + i][col + i] == checker for i in range(4))):
                return True
            if (col - 3 >= 0 and row + 3 < ROWS and
                all(board[row + i][col - i] == checker for i in range(4))):
                return True
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY_SPACE for col in range(COLS))

def main():
    board = create_board()
    current_player = PLAYER_ONE if random.randint(0, 1) == 0 else PLAYER_TWO
    while True:
        print_board(board)
        column = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        while not is_valid_input(column) or is_column_full(board, column_to_index(column)):
            if not is_valid_input(column):
                print("Invalid input. Please choose a column (A-G).")
            else:
                print("Column is full. Choose another column.")
            column = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        drop_checker(board, column_to_index(column), current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = PLAYER_ONE if current_player == PLAYER_TWO else PLAYER_TWO

if __name__ == "__main__":
    main()