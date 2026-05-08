# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 106
# filename        : gen_0106_gpt4mini_06.py
# timestamp       : 2026-04-06T09:01:10Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 586
# tokens_total    : 976
# cost_usd        : 0.000410
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

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
current_player = random.choice(["X", "O"])

def print_board():
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def valid_input(col):
    return col in "ABCDEFG" and board[0][ord(col) - 65] == " "

def drop_checker(col):
    for row in reversed(range(ROWS)):
        if board[row][ord(col) - 65] == " ":
            board[row][ord(col) - 65] = current_player
            return True
    return False

def check_win():
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == current_player and all(board[r][c + i] == current_player for i in range(4)):
                return True
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == current_player and all(board[r + i][c] == current_player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == current_player and all(board[r + i][c + i] == current_player for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] == current_player and all(board[r - i][c + i] == current_player for i in range(4)):
                return True
    return False

def is_full():
    return all(board[0][c] != " " for c in range(COLS))

while True:
    print_board()
    col = input(f"Player {current_player}, choose a column (A-G): ").upper()
    while not valid_input(col):
        col = input("Invalid input. Choose a column (A-G): ").upper()
    
    drop_checker(col)
    
    if check_win():
        print_board()
        print(f"Player {current_player} won!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break
    
    current_player = "O" if current_player == "X" else "X"