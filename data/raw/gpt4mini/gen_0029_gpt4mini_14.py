# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 29
# filename        : gen_0029_gpt4mini_14.py
# timestamp       : 2026-02-19T20:41:59Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 570
# tokens_total    : 957
# cost_usd        : 0.000400
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

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
current_player = random.randint(0, 1)

def print_board():
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print('|' + '|'.join(row) + '|')
        print("+---+---+---+---+---+---+---+")

def drop_checker(col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = 'X' if current_player == 0 else 'O'
            return True
    return False

def check_win():
    player_checker = 'X' if current_player == 0 else 'O'
    for r in range(ROWS):
        for c in range(COLS):
            if (c + 3 < COLS and all(board[r][c+i] == player_checker for i in range(4))) or \
               (r + 3 < ROWS and all(board[r+i][c] == player_checker for i in range(4))) or \
               (r + 3 < ROWS and c + 3 < COLS and all(board[r+i][c+i] == player_checker for i in range(4))) or \
               (r - 3 >= 0 and c + 3 < COLS and all(board[r-i][c+i] == player_checker for i in range(4))):
                return True
    return False

def is_full():
    return all(board[0][c] != ' ' for c in range(COLS))

def main():
    global current_player
    print_board()
    while True:
        col = input(f"Player {'X' if current_player == 0 else 'O'}, choose a column (A-G): ").upper()
        if col not in 'ABCDEFG':
            print("Invalid input! Please choose a letter from A to G.")
            continue
        col_idx = ord(col) - ord('A')
        if not drop_checker(col_idx):
            print("Column full! Choose another column.")
            continue
        print_board()
        if check_win():
            print(f"[{'X' if current_player == 0 else 'O'}] won!")
            break
        if is_full():
            print("It's a draw!")
            break
        current_player = 1 - current_player

if __name__ == "__main__":
    main()