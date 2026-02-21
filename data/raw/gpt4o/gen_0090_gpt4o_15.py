# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 90
# filename        : gen_0090_gpt4o_15.py
# timestamp       : 2026-02-19T21:03:21Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 388
# tokens_output   : 765
# tokens_total    : 1153
# cost_usd        : 0.008620
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
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_SLOT = ' '
PLAYER_MARKERS = ['X', 'O']

def create_board():
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLUMNS + '+')

def get_column_choice():
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if choice in COLUMN_LABELS:
            return COLUMN_LABELS.index(choice)
        print("Invalid choice. Please choose a column from A to G.")

def is_valid_move(board, column):
    return board[0][column] == EMPTY_SLOT

def drop_checker(board, column, marker):
    for row in reversed(board):
        if row[column] == EMPTY_SLOT:
            row[column] = marker
            return

def check_for_winner(board, marker):
    # Check horizontal
    for row in board:
        for col in range(COLUMNS - 3):
            if row[col] == row[col + 1] == row[col + 2] == row[col + 3] == marker:
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == marker:
                return True
    # Check diagonal /
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == marker:
                return True
    # Check diagonal \
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == marker:
                return True
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY_SLOT for col in range(COLUMNS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    while True:
        print_board(board)
        print(f"Player {PLAYER_MARKERS[current_player]}'s turn")
        column = get_column_choice()
        if not is_valid_move(board, column):
            print("Column is full. Try another one.")
            continue
        drop_checker(board, column, PLAYER_MARKERS[current_player])
        if check_for_winner(board, PLAYER_MARKERS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_MARKERS[current_player]} won!")
            break
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()