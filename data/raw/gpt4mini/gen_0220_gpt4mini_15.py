# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 220
# filename        : gen_0220_gpt4mini_15.py
# timestamp       : 2026-04-06T09:33:02Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 388
# tokens_output   : 668
# tokens_total    : 1056
# cost_usd        : 0.000459
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
#   Write in a straightforward, no-frills style.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_CHECKERS = ['X', 'O']

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def get_valid_column():
    while True:
        column = input("Choose a column (A-G): ").upper()
        if column in 'ABCDEFG':
            return ord(column) - ord('A')
        print("Invalid input. Please choose a column (A-G).")

def is_column_full(board, col):
    return board[0][col] != EMPTY

def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = checker
            return True
    return False

def check_winner(board, checker):
    # Check horizontal, vertical and diagonal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == checker for i in range(4)):
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == checker for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == checker for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == checker for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

def main():
    board = create_board()
    current_player = random.choice([0, 1])
    
    while True:
        print_board(board)
        print(f"Player {PLAYER_CHECKERS[current_player]}'s turn.")
        
        col = get_valid_column()
        while is_column_full(board, col):
            print("Column is full. Choose another column.")
            col = get_valid_column()

        drop_checker(board, col, PLAYER_CHECKERS[current_player])

        if check_winner(board, PLAYER_CHECKERS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_CHECKERS[current_player]} won!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()