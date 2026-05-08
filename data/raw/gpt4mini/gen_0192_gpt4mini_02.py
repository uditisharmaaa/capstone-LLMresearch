# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 192
# filename        : gen_0192_gpt4mini_02.py
# timestamp       : 2026-04-06T09:25:58Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 522
# tokens_total    : 911
# cost_usd        : 0.000372
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

def clear_screen(): os.system('clear')
def print_board():
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|".join(f" {cell} " for cell in row), "|")
        print("+---+---+---+---+---+---+---+")
def drop_checker(col, checker):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = checker
            return True
    return False
def valid_input(col):
    return col in "ABCDEFG" and board[0][ord(col) - 65] == ' '
def check_winner():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != ' ':
                if c + 3 < COLS and all(board[r][c + i] == board[r][c] for i in range(4)): return True
                if r + 3 < ROWS:
                    if all(board[r + i][c] == board[r][c] for i in range(4)): return True
                    if c + 3 < COLS and all(board[r + i][c + i] == board[r][c] for i in range(4)): return True
                    if c - 3 >= 0 and all(board[r + i][c - i] == board[r][c] for i in range(4)): return True
    return False
def is_draw():
    return all(board[0][c] != ' ' for c in range(COLS))

def main():
    player = random.choice(["X", "O"])
    while True:
        print_board()
        col = input(f"Player {player}, choose a column (A-G): ").upper()
        if valid_input(col):
            drop_checker(ord(col) - 65, player)
            if check_winner():
                print_board()
                print(f"Player {player} won!")
                break
            if is_draw():
                print_board()
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"

main()