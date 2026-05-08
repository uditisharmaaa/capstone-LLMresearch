# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 136
# filename        : gen_0136_gpt4mini_06.py
# timestamp       : 2026-04-06T09:08:15Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 556
# tokens_total    : 946
# cost_usd        : 0.000392
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
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
current_player = random.choice(['X', 'O'])

def print_board():
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---" + "+---" * (COLS - 1) + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" + "+---" * (COLS - 1) + "+")

def is_valid_input(col):
    return col in 'ABCDEFG' and board[0][ord(col) - 65] == ' '

def drop_checker(col):
    for row in range(ROWS-1, -1, -1):
        if board[row][ord(col) - 65] == ' ':
            board[row][ord(col) - 65] = current_player
            return row

def check_win(row, col):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for d in directions:
        count = 1
        for step in [1, -1]:
            r, c = row, col
            while 0 <= r + step * d[0] < ROWS and 0 <= c + step * d[1] < COLS and board[r + step * d[0]][c + step * d[1]] == current_player:
                count += 1
                r += step * d[0]
                c += step * d[1]
        if count >= 4:
            return True
    return False

def is_draw():
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    global current_player
    print_board()
    while True:
        col = input(f"Player {current_player}, choose a column (A-G): ").upper()
        while not is_valid_input(col):
            col = input(f"Invalid input. Player {current_player}, choose a column (A-G): ").upper()
        row = drop_checker(col)
        print_board()
        if check_win(row, ord(col) - 65):
            print(f"Player {current_player} won!")
            break
        if is_draw():
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()