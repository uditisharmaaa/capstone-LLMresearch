# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 146
# filename        : gen_0146_gpt4mini_01.py
# timestamp       : 2026-04-06T09:10:10Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 639
# tokens_total    : 1030
# cost_usd        : 0.000442
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" + "+---"*COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" + "+---"*COLS + "+")

def is_column_full(board, col):
    return board[0][col] != ' '

def drop_checker(board, col, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = symbol
            return

def is_winner(board, symbol):
    # Check horizontal, vertical, and diagonal
    for r in range(ROWS):
        for c in range(COLS):
            if c + 3 < COLS and all(board[r][c+i] == symbol for i in range(4)):
                return True
            if r + 3 < ROWS:
                if board[r][c] == symbol and all(board[r+i][c] == symbol for i in range(1, 4)):
                    return True
                if c + 3 < COLS and all(board[r+i][c+i] == symbol for i in range(4)):
                    return True
                if c - 3 >= 0 and all(board[r+i][c-i] == symbol for i in range(4)):
                    return True
    return False

def is_draw(board):
    return all(is_column_full(board, c) for c in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, 1)
    
    while True:
        print_board(board)
        current_symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {current_symbol}, choose a column (A-G): ")
        
        while True:
            choice = input().upper()
            if choice in COLUMN_LABELS:
                col = COLUMN_LABELS.index(choice)
                if not is_column_full(board, col):
                    drop_checker(board, col, current_symbol)
                    break
                else:
                    print("Column is full, choose another column.")
            else:
                print("Invalid input, please choose a column (A-G).")
        
        if is_winner(board, current_symbol):
            print_board(board)
            print(f"Player {current_symbol} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()