# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 2
# filename        : gen_0002_gpt4mini_02.py
# timestamp       : 2026-02-19T20:29:01Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 559
# tokens_total    : 948
# cost_usd        : 0.000394
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

import os
import random

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print("+---+---+---+---+---+---+---+")

def drop_checker(col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            return True
    return False

def is_winner(player):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True
    return False

def is_full():
    return all(board[0][c] != ' ' for c in range(COLS))

def get_valid_column():
    while True:
        col = input(f"Player {current_player}, choose a column (A-G): ").upper()
        if col in 'ABCDEFG':
            col_index = ord(col) - ord('A')
            if board[0][col_index] == ' ':
                return col_index
            else:
                print("Column is full! Try again.")
        else:
            print("Invalid input! Please choose A-G.")

current_player = random.choice(['X', 'O'])
print_board()

while True:
    col = get_valid_column()
    drop_checker(col, current_player)
    print_board()
    if is_winner(current_player):
        print(f"[{current_player}] won!")
        break
    if is_full():
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'