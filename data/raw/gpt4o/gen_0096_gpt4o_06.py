# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 96
# filename        : gen_0096_gpt4o_06.py
# timestamp       : 2026-02-19T21:04:33Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 596
# tokens_total    : 986
# cost_usd        : 0.006935
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

import os
import random

ROWS, COLS = 6, 7
PLAYERS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def initialize_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def is_valid_input(column):
    return column in COLUMN_LABELS

def is_column_full(board, col_index):
    return board[0][col_index] != ' '

def get_lowest_row(board, col_index):
    for row in range(ROWS-1, -1, -1):
        if board[row][col_index] == ' ':
            return row
    return -1

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS):
            if (col <= COLS-4 and all(board[row][col+i] == player for i in range(4))) or \
               (row <= ROWS-4 and all(board[row+i][col] == player for i in range(4))) or \
               (row <= ROWS-4 and col <= COLS-4 and all(board[row+i][col+i] == player for i in range(4))) or \
               (row >= 3 and col <= COLS-4 and all(board[row-i][col+i] == player for i in range(4))):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    board = initialize_board()
    current_player = random.choice(PLAYERS)
    while True:
        print_board(board)
        print(f"{current_player}'s turn:")
        column = input("Choose column (A-G): ").strip().upper()
        if not is_valid_input(column) or is_column_full(board, COLUMN_LABELS.index(column)):
            print("Invalid input. Try again.")
            continue
        col_index = COLUMN_LABELS.index(column)
        row_index = get_lowest_row(board, col_index)
        board[row_index][col_index] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} won!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = PLAYERS[1] if current_player == PLAYERS[0] else PLAYERS[0]

if __name__ == "__main__":
    main()