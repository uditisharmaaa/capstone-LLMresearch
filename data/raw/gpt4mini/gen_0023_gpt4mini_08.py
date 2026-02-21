# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 23
# filename        : gen_0023_gpt4mini_08.py
# timestamp       : 2026-02-19T20:36:32Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 389
# tokens_output   : 712
# tokens_total    : 1101
# cost_usd        : 0.000486
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

# Constants for board dimensions and players
ROWS = 6
COLS = 7
PLAYER_COUNT = 2
EMPTY_SPACE = ' '
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def initialize_board():
    return [[EMPTY_SPACE for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" + "+---" * (COLS - 1) + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" + "+---" * (COLS - 1) + "+")

def is_valid_input(column, board):
    if column not in COLUMN_LABELS:
        return False
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] == EMPTY_SPACE

def drop_checker(board, column, player_symbol):
    col_index = COLUMN_LABELS.index(column)
    for row in reversed(board):
        if row[col_index] == EMPTY_SPACE:
            row[col_index] = player_symbol
            return True
    return False

def check_winner(board, player_symbol):
    # Check horizontal, vertical, and diagonal for a win
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player_symbol for i in range(4)):
                return True
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_symbol for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player_symbol for i in range(4)):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player_symbol for i in range(4)):
                return True
    return False

def is_full(board):
    return all(board[0][col] != EMPTY_SPACE for col in range(COLS))

def main():
    board = initialize_board()
    current_player = random.randint(0, PLAYER_COUNT - 1)

    while True:
        print_board(board)
        player_symbol = PLAYER_SYMBOLS[current_player]
        column = input(f"Player {player_symbol}, choose a column (A-G): ").upper()

        while not is_valid_input(column, board):
            print("Invalid input. Please choose a valid column (A-G) that is not full.")
            column = input(f"Player {player_symbol}, choose a column (A-G): ").upper()

        drop_checker(board, column, player_symbol)

        if check_winner(board, player_symbol):
            print_board(board)
            print(f"Player {player_symbol} won!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYER_COUNT

if __name__ == "__main__":
    main()