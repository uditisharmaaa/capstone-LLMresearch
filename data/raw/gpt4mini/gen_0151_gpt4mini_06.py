# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 151
# filename        : gen_0151_gpt4mini_06.py
# timestamp       : 2026-04-06T09:11:08Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 531
# tokens_total    : 921
# cost_usd        : 0.000377
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
BOARD = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def clear_screen():
    os.system('clear')

def print_board():
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in BOARD:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def drop_checker(col, player):
    for row in reversed(BOARD):
        if row[col] == ' ':
            row[col] = player
            return True
    return False

def check_winner(player):
    for r in range(ROWS):
        for c in range(COLS):
            if (c <= COLS - 4 and all(BOARD[r][c+i] == player for i in range(4))) or \
               (r <= ROWS - 4 and all(BOARD[r+i][c] == player for i in range(4))) or \
               (r <= ROWS - 4 and c <= COLS - 4 and all(BOARD[r+i][c+i] == player for i in range(4))) or \
               (r >= 3 and c <= COLS - 4 and all(BOARD[r-i][c+i] == player for i in range(4))):
                return True
    return False

def is_full():
    return all(BOARD[0][c] != ' ' for c in range(COLS))

def main():
    current_player = random.choice(['X', 'O'])
    while True:
        print_board()
        col = input(f"Player {current_player}, choose a column (A-G): ").upper()
        if col not in "ABCDEFG":
            print("Invalid input. Try again.")
            continue
        col_index = ord(col) - ord('A')
        if not drop_checker(col_index, current_player):
            print("Column full. Try again.")
            continue
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} won!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()