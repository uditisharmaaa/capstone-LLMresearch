# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 85
# filename        : gen_0085_gpt4o_10.py
# timestamp       : 2026-02-19T21:02:12Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 390
# tokens_output   : 721
# tokens_total    : 1111
# cost_usd        : 0.008185
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

import os
import random

BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2
EMPTY_CELL = ' '

def create_board():
    return [[EMPTY_CELL for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join([chr(65 + i) for i in range(BOARD_COLS)]))
    print("+---" * BOARD_COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * BOARD_COLS + "+")

def is_valid_input(choice):
    return choice in [chr(65 + i) for i in range(BOARD_COLS)]

def is_column_full(board, col):
    return all(row[col] != EMPTY_CELL for row in board)

def get_next_open_row(board, col):
    for r in range(BOARD_ROWS - 1, -1, -1):
        if board[r][col] == EMPTY_CELL:
            return r
    return None

def place_checker(board, row, col, checker):
    board[row][col] = checker

def winning_move(board, checker):
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS):
            if all(board[r][c+i] == checker for i in range(4)):
                return True
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS - 3):
            if all(board[r+i][c] == checker for i in range(4)):
                return True
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS - 3):
            if all(board[r+i][c+i] == checker for i in range(4)):
                return True
    for c in range(BOARD_COLS - 3):
        for r in range(3, BOARD_ROWS):
            if all(board[r-i][c+i] == checker for i in range(4)):
                return True
    return False

def board_full(board):
    return all(board[0][c] != EMPTY_CELL for c in range(BOARD_COLS))

def get_player_input(board, player):
    while True:
        choice = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if not is_valid_input(choice):
            print("Invalid input. Please choose a letter from A to G.")
            continue
        col = ord(choice) - ord('A')
        if is_column_full(board, col):
            print("Column full. Choose another column.")
            continue
        return col

def main():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    
    while True:
        print_board(board)
        col = get_player_input(board, current_player)
        row = get_next_open_row(board, col)
        place_checker(board, row, col, current_player)

        if winning_move(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break

        if board_full(board):
            print_board(board)
            print("The game is a draw.")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()