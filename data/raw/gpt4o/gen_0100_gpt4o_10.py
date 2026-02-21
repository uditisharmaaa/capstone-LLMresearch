# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 100
# filename        : gen_0100_gpt4o_10.py
# timestamp       : 2026-02-19T21:05:30Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 390
# tokens_output   : 774
# tokens_total    : 1164
# cost_usd        : 0.008715
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

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+' + '---+' * COLUMNS)
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+' + '---+' * COLUMNS)

def choose_first_player():
    return random.randint(0, PLAYERS - 1)

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, column):
    column_index = COLUMN_LABELS.index(column)
    return board[0][column_index] != EMPTY

def get_next_open_row(board, column_index):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column_index] == EMPTY:
            return row
    return None

def make_move(board, column, player_symbol):
    column_index = COLUMN_LABELS.index(column)
    row = get_next_open_row(board, column_index)
    if row is not None:
        board[row][column_index] = player_symbol

def check_for_win(board, player_symbol):
    # Check horizontal locations
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player_symbol for i in range(4)):
                return True
    # Check vertical locations
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_symbol for i in range(4)):
                return True
    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player_symbol for i in range(4)):
                return True
    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player_symbol for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

def get_player_input():
    while True:
        player_input = input("Choose a column (A-G): ").strip().upper()
        if len(player_input) == 1 and is_valid_column(player_input):
            return player_input
        print("Invalid input. Please enter a letter between A and G.")

def main():
    board = create_board()
    current_player_index = choose_first_player()
    print_board(board)

    while True:
        current_symbol = PLAYER_SYMBOLS[current_player_index]
        column = get_player_input()

        if is_column_full(board, column):
            print("Column is full. Try a different column.")
            continue

        make_move(board, column, current_symbol)
        print_board(board)

        if check_for_win(board, current_symbol):
            print(f"{current_symbol} won!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player_index = (current_player_index + 1) % PLAYERS

if __name__ == "__main__":
    main()