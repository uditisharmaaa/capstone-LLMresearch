# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 161
# filename        : gen_0161_gpt4mini_01.py
# timestamp       : 2026-04-06T09:13:31Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 698
# tokens_total    : 1089
# cost_usd        : 0.000477
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

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def is_valid_input(column, board):
    if len(column) != 1 or column not in "ABCDEFG":
        return False
    col_index = ord(column) - ord('A')
    if board[0][col_index] != ' ':
        return False
    return True

def drop_checker(board, column, checker):
    col_index = ord(column) - ord('A')
    for row in reversed(board):
        if row[col_index] == ' ':
            row[col_index] = checker
            return True
    return False

def check_winner(board, checker):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == checker for i in range(4)):
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == checker for i in range(4)):
                return True

    # Check diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == checker for i in range(4)):
                return True

    # Check diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == checker for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    checkers = ['X', 'O']
    
    print_board(board)
    
    while True:
        player_checker = checkers[current_player]
        column = input(f"Player {player_checker}, choose a column (A-G): ").upper()
        
        while not is_valid_input(column, board):
            print("Invalid input. Please choose a column (A-G) that is not full.")
            column = input(f"Player {player_checker}, choose a column (A-G): ").upper()
        
        drop_checker(board, column, player_checker)
        print_board(board)

        if check_winner(board, player_checker):
            print(f"Player {player_checker} won!")
            break
        
        if is_board_full(board):
            print("The game is a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()