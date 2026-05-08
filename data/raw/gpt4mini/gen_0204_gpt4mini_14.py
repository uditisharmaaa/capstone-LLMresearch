# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 204
# filename        : gen_0204_gpt4mini_14.py
# timestamp       : 2026-04-06T09:28:56Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 544
# tokens_total    : 931
# cost_usd        : 0.000384
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

import os
import random

ROWS, COLS, P = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']
turn = random.randint(0, 1)

def print_board():
    os.system('clear')
    print("  A B C D E F G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|" + "|".join(row) + "|")
        print("+---+---+---+---+---+---+---+")

def valid_input(col):
    if col not in 'ABCDEFG':
        return False
    idx = ord(col) - ord('A')
    return board[0][idx] == ' '

def drop_checker(col):
    idx = ord(col) - ord('A')
    for r in range(ROWS-1, -1, -1):
        if board[r][idx] == ' ':
            board[r][idx] = players[turn]
            return True
    return False

def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != ' ':
                if c + 3 < COLS and all(board[r][c+i] == board[r][c] for i in range(4)):
                    return True
                if r + 3 < ROWS:
                    if all(board[r+i][c] == board[r][c] for i in range(4)):
                        return True
                    if c + 3 < COLS and all(board[r+i][c+i] == board[r][c] for i in range(4)):
                        return True
                    if c - 3 >= 0 and all(board[r+i][c-i] == board[r][c] for i in range(4)):
                        return True
    return False

def check_draw():
    return all(board[0][c] != ' ' for c in range(COLS))

while True:
    print_board()
    col = input(f"Player {players[turn]}, choose a column (A-G): ").strip().upper()
    if valid_input(col):
        if drop_checker(col):
            if check_win():
                print_board()
                print(f"Player {players[turn]} won!")
                break
            if check_draw():
                print_board()
                print("It's a draw!")
                break
            turn = (turn + 1) % P
    else:
        print("Invalid input, try again.")