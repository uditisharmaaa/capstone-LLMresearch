# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 111
# filename        : gen_0111_gpt4mini_11.py
# timestamp       : 2026-04-06T09:02:45Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 774
# tokens_total    : 1161
# cost_usd        : 0.000522
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
#   Write with extensive docstrings for every function.
# ====================================================================

import os
import random

BOARD_ROWS = 6
BOARD_COLS = 7
PLAYERS = 2

def create_board():
    """Create a 2D board initialized with spaces."""
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    """Print the current state of the board with column labels."""
    os.system('clear')  # Clear the console
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column, board):
    """Check if the input column is valid."""
    if column not in 'ABCDEFG':
        return False
    col_index = ord(column) - ord('A')
    if board[0][col_index] != ' ':
        return False
    return True

def drop_checker(board, column, checker):
    """Drop the checker into the specified column."""
    col_index = ord(column) - ord('A')
    for row in reversed(board):
        if row[col_index] == ' ':
            row[col_index] = checker
            return

def check_winner(board, checker):
    """Check if the given checker has won the game."""
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(board[0][col] != ' ' for col in range(BOARD_COLS))

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)

    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        column = input("Choose a column (A-G): ").upper()

        while not is_valid_input(column, board):
            print("Invalid input. Please choose a valid column (A-G) that is not full.")
            column = input("Choose a column (A-G): ").upper()

        drop_checker(board, column, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()