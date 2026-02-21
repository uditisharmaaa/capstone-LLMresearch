# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 19
# filename        : gen_0019_gpt4o_04.py
# timestamp       : 2026-02-19T20:35:42Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 652
# tokens_total    : 1043
# cost_usd        : 0.007498
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
EMPTY_SLOT = ' '

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(chr(65 + i) for i in range(COLUMNS)))
    for row in board:
        print("+---" * COLUMNS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * COLUMNS + "+")

def select_first_player():
    return random.choice(['X', 'O'])

def is_valid_input(column):
    return column in 'ABCDEFG'

def is_column_full(board, column_index):
    return board[0][column_index] != EMPTY_SLOT

def drop_checker(board, column_index, checker):
    for row in reversed(board):
        if row[column_index] == EMPTY_SLOT:
            row[column_index] = checker
            return True
    return False

def check_for_winner(board, checker):
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY_SLOT for col in range(COLUMNS))

def main():
    board = create_board()
    current_player = select_first_player()
    
    while True:
        print_board(board)
        print(f"{current_player}'s turn. Choose a column (A-G):")
        column = input().strip().upper()
        
        if not is_valid_input(column):
            print("Invalid input. Please enter a letter from A to G.")
            continue
        
        column_index = ord(column) - 65
        if is_column_full(board, column_index):
            print("Column is full. Please choose another column.")
            continue

        drop_checker(board, column_index, current_player)

        if check_for_winner(board, current_player):
            print_board(board)
            print(f"{current_player} won!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()