# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 176
# filename        : gen_0176_gpt4mini_01.py
# timestamp       : 2026-04-06T09:22:04Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 674
# tokens_total    : 1065
# cost_usd        : 0.000463
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

ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def is_valid_input(col):
    return col in 'ABCDEFG'

def get_column_index(col):
    return ord(col) - ord('A')

def is_column_full(board, col_index):
    return board[0][col_index] != EMPTY

def drop_checker(board, col_index, checker):
    for row in reversed(board):
        if row[col_index] == EMPTY:
            row[col_index] = checker
            break

def check_winner(board, checker):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == checker for i in range(4)):
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == checker for i in range(4)):
                return True

    # Check diagonal (/)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == checker for i in range(4)):
                return True

    # Check diagonal (\)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == checker for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

def main():
    board = create_board()
    current_player = random.choice([PLAYER_X, PLAYER_O])
    print_board(board)

    while True:
        col = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        if not is_valid_input(col):
            print("Invalid input. Please choose a letter from A to G.")
            continue
        
        col_index = get_column_index(col)
        
        if is_column_full(board, col_index):
            print("Column is full. Try a different column.")
            continue
        
        drop_checker(board, col_index, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        
        if is_board_full(board):
            print("The game is a draw!")
            break
        
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    main()