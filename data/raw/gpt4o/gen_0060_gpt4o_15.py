# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 60
# filename        : gen_0060_gpt4o_15.py
# timestamp       : 2026-02-19T20:48:56Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 388
# tokens_output   : 639
# tokens_total    : 1027
# cost_usd        : 0.007360
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

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(['   ' if cell == ' ' else f' {cell} ' for cell in row]) + '|')
        print('+---' * COLUMNS + '+')

def select_starting_player():
    return random.choice(['X', 'O'])

def is_valid_input(input_str):
    return input_str in COLUMN_LABELS

def is_column_full(board, column_index):
    return board[0][column_index] != ' '

def get_column_index(column_label):
    return COLUMN_LABELS.index(column_label)

def drop_checker(board, column_index, checker):
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = checker
            break

def check_win(board, checker):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == checker:
                if col <= COLUMNS - 4 and all(board[row][col + i] == checker for i in range(4)):
                    return True
                if row <= ROWS - 4 and all(board[row + i][col] == checker for i in range(4)):
                    return True
                if col <= COLUMNS - 4 and row <= ROWS - 4 and all(board[row + i][col + i] == checker for i in range(4)):
                    return True
                if col >= 3 and row <= ROWS - 4 and all(board[row + i][col - i] == checker for i in range(4)):
                    return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def main():
    board = create_board()
    current_player = select_starting_player()
    print_board(board)
    
    while True:
        move = input(f"Player {current_player}, enter a column (A-G): ").strip().upper()
        if not is_valid_input(move):
            continue
        column_index = get_column_index(move)
        if is_column_full(board, column_index):
            continue
        drop_checker(board, column_index, current_player)
        print_board(board)
        
        if check_win(board, current_player):
            print(f"{current_player} won!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()