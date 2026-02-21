# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 79
# filename        : gen_0079_gpt4o_04.py
# timestamp       : 2026-02-19T21:01:02Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 704
# tokens_total    : 1095
# cost_usd        : 0.008018
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

BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * BOARD_COLS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * BOARD_COLS + '+')

def get_column_index(column_label):
    if column_label in COLUMN_LABELS:
        return COLUMN_LABELS.index(column_label)
    return -1

def is_valid_column(column_index, board):
    return 0 <= column_index < BOARD_COLS and board[0][column_index] == ' '

def drop_checker(column_index, player, board):
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = player
            return

def check_winner(board, player):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if check_direction(board, player, row, col, 1, 0) or \
               check_direction(board, player, row, col, 0, 1) or \
               check_direction(board, player, row, col, 1, 1) or \
               check_direction(board, player, row, col, 1, -1):
                return True
    return False

def check_direction(board, player, start_row, start_col, delta_row, delta_col):
    count = 0
    for i in range(4):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS and board[row][col] == player:
            count += 1
        else:
            break
    return count == 4

def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(BOARD_COLS))

def play_connect_4():
    board = create_board()
    current_player = random.choice(PLAYER_SYMBOLS)
    print_board(board)

    while True:
        column_label = input(f"Player {current_player}, choose a column (A-G): ").strip().upper()
        column_index = get_column_index(column_label)

        if column_index == -1 or not is_valid_column(column_index, board):
            print("Invalid input. Please choose a valid column.")
            continue

        drop_checker(column_index, current_player, board)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break

        if is_board_full(board):
            print("The game is a draw!")
            break

        current_player = PLAYER_SYMBOLS[(PLAYER_SYMBOLS.index(current_player) + 1) % NUM_PLAYERS]

if __name__ == '__main__':
    play_connect_4()