# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 94
# filename        : gen_0094_gpt4o_04.py
# timestamp       : 2026-02-19T21:04:13Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 807
# tokens_total    : 1198
# cost_usd        : 0.009047
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

import os
import random

ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def initialize_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+' + '---+' * COLUMNS)
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+' + '---+' * COLUMNS)

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, column_index):
    return all(row[column_index] != ' ' for row in board)

def get_column_index(column):
    return COLUMN_LABELS.index(column)

def make_move(board, column_index, player_symbol):
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = player_symbol
            return

def check_winner(board, player_symbol):
    def check_line(start_row, start_col, delta_row, delta_col):
        count = 0
        row, col = start_row, start_col
        while 0 <= row < ROWS and 0 <= col < COLUMNS:
            if board[row][col] == player_symbol:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            row += delta_row
            col += delta_col
        return False

    for row in range(ROWS):
        if check_line(row, 0, 0, 1):  # Horizontal
            return True
    for col in range(COLUMNS):
        if check_line(0, col, 1, 0):  # Vertical
            return True
    for row in range(ROWS):
        if check_line(row, 0, 1, 1):  # Diagonal /
            return True
        if check_line(row, COLUMNS - 1, 1, -1):  # Diagonal \
            return True
    for col in range(COLUMNS):
        if check_line(0, col, 1, 1):  # Diagonal /
            return True
        if check_line(0, col, 1, -1):  # Diagonal \
            return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def main():
    board = initialize_board()
    current_player = random.randint(0, PLAYERS - 1)

    while True:
        print_board(board)
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn.")
        while True:
            column = input('Choose a column (A-G): ').strip().upper()
            if not is_valid_column(column):
                print('Invalid column. Please choose a letter from A to G.')
                continue
            column_index = get_column_index(column)
            if is_column_full(board, column_index):
                print('Column is full. Please choose another column.')
                continue
            break

        make_move(board, column_index, PLAYER_SYMBOLS[current_player])

        if check_winner(board, PLAYER_SYMBOLS[current_player]):
            print_board(board)
            print(f'Player {PLAYER_SYMBOLS[current_player]} won!')
            break

        if is_draw(board):
            print_board(board)
            print('The game is a draw!')
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == '__main__':
    main()