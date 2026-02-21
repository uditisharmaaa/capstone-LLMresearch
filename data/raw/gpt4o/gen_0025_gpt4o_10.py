# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 25
# filename        : gen_0025_gpt4o_10.py
# timestamp       : 2026-02-19T20:40:51Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 390
# tokens_output   : 819
# tokens_total    : 1209
# cost_usd        : 0.009165
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
BOARD_COLUMNS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

def clear_screen():
    os.system('clear')

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * BOARD_COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * BOARD_COLUMNS + '+')

def select_random_player():
    return random.choice([0, 1])

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, column):
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] != ' '

def get_next_open_row(board, column):
    col_index = COLUMN_LABELS.index(column)
    for row in range(BOARD_ROWS-1, -1, -1):
        if board[row][col_index] == ' ':
            return row
    return -1

def drop_checker(board, row, column, player):
    col_index = COLUMN_LABELS.index(column)
    board[row][col_index] = PLAYER_SYMBOLS[player]

def check_winner(board, player):
    symbol = PLAYER_SYMBOLS[player]
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row][c] == symbol for c in range(col, col + 4)):
                return True
    # Check vertical
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS - 3):
            if all(board[r][col] == symbol for r in range(row, row + 4)):
                return True
    # Check positively sloped diagonals
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row + i][col + i] == symbol for i in range(4)):
                return True
    # Check negatively sloped diagonals
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row - i][col + i] == symbol for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(BOARD_COLUMNS))

def get_player_input():
    while True:
        column = input("Choose a column (A-G): ").strip().upper()
        if is_valid_column(column):
            return column
        else:
            print("Invalid input. Please enter a letter between A and G.")

def play_game():
    board = create_board()
    current_player = select_random_player()
    while True:
        print_board(board)
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn.")
        column = get_player_input()
        
        if is_column_full(board, column):
            print("Column is full. Choose another column.")
            continue
        
        row = get_next_open_row(board, column)
        drop_checker(board, row, column, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == '__main__':
    play_game()