# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 228
# filename        : gen_0228_gpt4mini_08.py
# timestamp       : 2026-04-06T10:20:35Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 389
# tokens_output   : 754
# tokens_total    : 1143
# cost_usd        : 0.000511
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
#   Write with a focus on code readability over brevity.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column):
    return column in 'ABCDEFG'

def is_column_full(board, col):
    return board[0][col] != EMPTY

def drop_checker(board, col, checker):
    for row in reversed(range(ROWS)):
        if board[row][col] == EMPTY:
            board[row][col] = checker
            return True
    return False

def check_win(board, checker):
    for row in range(ROWS):
        for col in range(COLS):
            if (check_horizontal(board, row, col, checker) or
                check_vertical(board, row, col, checker) or
                check_diagonal(board, row, col, checker)):
                return True
    return False

def check_horizontal(board, row, col, checker):
    if col + 3 < COLS:
        return all(board[row][col + i] == checker for i in range(4))
    return False

def check_vertical(board, row, col, checker):
    if row + 3 < ROWS:
        return all(board[row + i][col] == checker for i in range(4))
    return False

def check_diagonal(board, row, col, checker):
    if col + 3 < COLS and row + 3 < ROWS:
        if all(board[row + i][col + i] == checker for i in range(4)):
            return True
    if col - 3 >= 0 and row + 3 < ROWS:
        if all(board[row + i][col - i] == checker for i in range(4)):
            return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = create_board()
    current_player = random.choice(['X', 'O'])
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        column = input("Choose a column (A-G): ").upper()
        
        while not is_valid_input(column):
            column = input("Invalid input. Choose a column (A-G): ").upper()
        
        col_index = ord(column) - ord('A')
        
        while is_column_full(board, col_index):
            column = input("Column full. Choose a different column (A-G): ").upper()
            while not is_valid_input(column):
                column = input("Invalid input. Choose a column (A-G): ").upper()
            col_index = ord(column) - ord('A')
        
        drop_checker(board, col_index, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()