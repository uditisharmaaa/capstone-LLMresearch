# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 196
# filename        : gen_0196_gpt4mini_06.py
# timestamp       : 2026-04-06T09:27:05Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 616
# tokens_total    : 1006
# cost_usd        : 0.000428
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

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column, board):
    if column not in 'ABCDEFG':
        return False
    col_index = ord(column) - ord('A')
    if board[0][col_index] != ' ':
        return False
    return True

def drop_checker(board, column, symbol):
    col_index = ord(column) - ord('A')
    for row in reversed(board):
        if row[col_index] == ' ':
            row[col_index] = symbol
            return True
    return False

def check_winner(board, symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if (c + 3 < COLS and all(board[r][c + i] == symbol for i in range(4))) or \
               (r + 3 < ROWS and all(board[r + i][c] == symbol for i in range(4))) or \
               (r + 3 < ROWS and c + 3 < COLS and all(board[r + i][c + i] == symbol for i in range(4))) or \
               (r - 3 >= 0 and c + 3 < COLS and all(board[r - i][c + i] == symbol for i in range(4))):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, 1)
    
    while True:
        print_board(board)
        column = input(f"Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").upper()
        
        while not is_valid_input(column, board):
            column = input("Invalid input. Choose a column (A-G): ").upper()
        
        drop_checker(board, column, PLAYER_SYMBOLS[current_player])
        
        if check_winner(board, PLAYER_SYMBOLS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()