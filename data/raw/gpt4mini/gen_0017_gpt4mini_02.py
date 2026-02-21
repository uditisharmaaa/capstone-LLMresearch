# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 17
# filename        : gen_0017_gpt4mini_02.py
# timestamp       : 2026-02-19T20:35:04Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 510
# tokens_total    : 899
# cost_usd        : 0.000364
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
current_player = random.randint(0, 1)

def print_board():
    os.system('clear')
    print("   " + "   ".join(chr(65 + i) for i in range(COLS)))
    print("+---+" + "---+".join([''] * COLS))
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+" + "---+".join([''] * COLS))

def drop_checker(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = 'X' if current_player == 0 else 'O'
            return row
    return -1

def check_win(row, col):
    checker = board[row][col]
    for dr, dc in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        count = 1
        for d in [1, -1]:
            r, c = row, col
            while 0 <= r + d * dr < ROWS and 0 <= c + d * dc < COLS and board[r + d * dr][c + d * dc] == checker:
                count += 1
                r += d * dr
                c += d * dc
        if count >= 4:
            return True
    return False

def full_board():
    return all(board[0][col] != ' ' for col in range(COLS))

while True:
    print_board()
    col_input = input(f"Player {'X' if current_player == 0 else 'O'}, choose a column (A-G): ").upper()
    if col_input not in "ABCDEFG":
        continue
    col = ord(col_input) - 65
    if drop_checker(col) == -1:
        continue
    if check_win(ROWS - 1, col):
        print_board()
        print(f"Player {'X' if current_player == 0 else 'O'} won!")
        break
    if full_board():
        print_board()
        print("It's a draw!")
        break
    current_player = 1 - current_player