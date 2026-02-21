# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 75
# filename        : gen_0075_gpt4o_15.py
# timestamp       : 2026-02-19T21:00:13Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 388
# tokens_output   : 631
# tokens_total    : 1019
# cost_usd        : 0.007280
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
#   Write in a straightforward, no-frills style.
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
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def choose_column():
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if choice in "ABCDEFG":
            return ord(choice) - ord('A')
        else:
            print("Invalid input. Please choose a letter between A and G.")

def is_valid_move(board, col):
    return board[0][col] == EMPTY

def make_move(board, col, symbol):
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = symbol
            return

def check_winner(board, symbol):
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c + i] == symbol for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if all(board[r + i][c] == symbol for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r + i][c + i] == symbol for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r - i][c + i] == symbol for i in range(4)):
                return True
    return False

def main():
    board = create_board()
    current_player_index = random.choice([0, 1])
    print_board(board)

    while True:
        print(f"Player {PLAYER_SYMBOLS[current_player_index]}'s turn")
        col = choose_column()
        if not is_valid_move(board, col):
            print("Column is full. Choose another column.")
            continue
        make_move(board, col, PLAYER_SYMBOLS[current_player_index])
        print_board(board)

        if check_winner(board, PLAYER_SYMBOLS[current_player_index]):
            print(f"{PLAYER_SYMBOLS[current_player_index]} won!")
            break

        if all(board[0][col] != EMPTY for col in range(COLUMNS)):
            print("It's a draw!")
            break

        current_player_index = (current_player_index + 1) % PLAYERS

if __name__ == "__main__":
    main()