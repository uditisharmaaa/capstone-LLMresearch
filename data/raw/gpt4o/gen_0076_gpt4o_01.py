# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 76
# filename        : gen_0076_gpt4o_01.py
# timestamp       : 2026-02-19T21:00:26Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 770
# tokens_total    : 1161
# cost_usd        : 0.008678
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
COLUMNS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    for row in board:
        print("+---" * COLUMNS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * COLUMNS + "+")

def get_column_index(letter):
    return ord(letter) - ord('A')

def is_valid_column(column):
    return 0 <= column < COLUMNS

def is_column_full(board, column):
    return board[0][column] != EMPTY

def drop_checker(board, column, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = symbol
            return

def check_winner(board, symbol):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if (check_horizontal(board, row, col, symbol) or
                check_vertical(board, row, col, symbol) or
                check_diagonal(board, row, col, symbol)):
                return True
    return False

def check_horizontal(board, row, col, symbol):
    if col + 3 < COLUMNS and all(board[row][col+i] == symbol for i in range(4)):
        return True
    return False

def check_vertical(board, row, col, symbol):
    if row + 3 < ROWS and all(board[row+i][col] == symbol for i in range(4)):
        return True
    return False

def check_diagonal(board, row, col, symbol):
    if row + 3 < ROWS and col + 3 < COLUMNS and all(board[row+i][col+i] == symbol for i in range(4)):
        return True
    if row + 3 < ROWS and col - 3 >= 0 and all(board[row+i][col-i] == symbol for i in range(4)):
        return True
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

def get_player_input():
    while True:
        column_letter = input("Choose a column (A-G): ").strip().upper()
        if len(column_letter) == 1 and 'A' <= column_letter <= 'G':
            return column_letter
        print("Invalid input. Please enter a letter between A and G.")

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)

    while True:
        print_board(board)
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn")
        
        column_letter = get_player_input()
        column = get_column_index(column_letter)

        if not is_valid_column(column) or is_column_full(board, column):
            print("Column full or invalid. Choose another column.")
            continue

        drop_checker(board, column, PLAYER_SYMBOLS[current_player])

        if check_winner(board, PLAYER_SYMBOLS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()