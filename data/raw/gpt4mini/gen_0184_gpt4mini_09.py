# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 184
# filename        : gen_0184_gpt4mini_09.py
# timestamp       : 2026-04-06T09:24:02Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 391
# tokens_output   : 671
# tokens_total    : 1062
# cost_usd        : 0.000461
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_SPACE = " "

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
    return column in "ABCDEFG"

def is_column_full(board, col):
    return board[0][col] != EMPTY_SPACE

def drop_checker(board, col, checker):
    for row in reversed(board):
        if row[col] == EMPTY_SPACE:
            row[col] = checker
            return

def check_winner(board, checker):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == checker for i in range(4)):
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == checker for i in range(4)):
                return True

    # Check diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == checker for i in range(4)):
                return True

    # Check diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == checker for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][c] != EMPTY_SPACE for c in range(COLS))

def main():
    board = create_board()
    current_player = random.choice([PLAYER_X, PLAYER_O])
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn. Choose a column (A-G):")
        
        while True:
            column_input = input().upper()
            if is_valid_input(column_input):
                column = ord(column_input) - ord('A')
                if not is_column_full(board, column):
                    drop_checker(board, column, current_player)
                    break
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid input. Please choose a column (A-G).")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    main()