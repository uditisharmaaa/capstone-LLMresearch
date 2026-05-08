# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 121
# filename        : gen_0121_gpt4mini_06.py
# timestamp       : 2026-04-06T09:05:07Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 549
# tokens_total    : 939
# cost_usd        : 0.000388
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

def is_full(col):
    return board[0][col] != " "

def drop_checker(col):
    for row in reversed(range(ROWS)):
        if board[row][col] == " ":
            board[row][col] = current_player
            return row

def check_win(row, col):
    def check_direction(delta_row, delta_col):
        count = 0
        for d in range(-3, 4):
            r, c = row + d * delta_row, col + d * delta_col
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == current_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    return (check_direction(0, 1) or 
            check_direction(1, 0) or 
            check_direction(1, 1) or 
            check_direction(1, -1))

def is_draw():
    return all(is_full(col) for col in range(COLS))

def get_column():
    while True:
        choice = input(f"Player {current_player}, choose a column (A-G): ").upper()
        if choice in "ABCDEFG":
            col = ord(choice) - ord('A')
            if not is_full(col):
                return col
            else:
                print("Column is full. Choose another.")
        else:
            print("Invalid input. Choose a letter from A to G.")

def main():
    print_board()
    while True:
        col = get_column()
        row = drop_checker(col)
        print_board()
        if check_win(row, col):
            print(f"{current_player} won!")
            break
        if is_draw():
            print("It's a draw!")
            break
        global current_player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()