# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 141
# filename        : gen_0141_gpt4mini_11.py
# timestamp       : 2026-04-06T09:09:15Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 779
# tokens_total    : 1166
# cost_usd        : 0.000525
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
#   Write with extensive docstrings for every function.
# ====================================================================

import os
import random

# Constants for the board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

def create_board():
    """Creates a 2D board initialized with spaces."""
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the current state of the board with column labels A-G."""
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(col_input):
    """Validates the player's input for column selection."""
    if len(col_input) != 1 or col_input not in "ABCDEFG":
        return False
    return True

def get_column_index(col_input):
    """Converts column letter (A-G) to index (0-6)."""
    return ord(col_input) - ord('A')

def is_column_full(board, col):
    """Checks if the specified column is full."""
    return board[0][col] != ' '

def drop_checker(board, col, checker):
    """Drops the checker into the lowest available row in the specified column."""
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = checker
            return row

def check_win(board, checker):
    """Checks for a win condition for the specified checker."""
    # Check horizontal, vertical, and diagonal wins
    for row in range(ROWS):
        for col in range(COLS):
            if (col <= COLS - 4 and all(board[row][col+i] == checker for i in range(4))) or \
               (row <= ROWS - 4 and all(board[row+i][col] == checker for i in range(4))) or \
               (row <= ROWS - 4 and col <= COLS - 4 and all(board[row+i][col+i] == checker for i in range(4))) or \
               (row >= 3 and col <= COLS - 4 and all(board[row-i][col+i] == checker for i in range(4))):
                return True
    return False

def is_draw(board):
    """Checks if the board is full and there is no winner."""
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    
    print_board(board)
    
    while True:
        col_input = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        while not is_valid_input(col_input) or is_column_full(board, get_column_index(col_input)):
            print("Invalid input. Please choose a valid column (A-G) that is not full.")
            col_input = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        col_index = get_column_index(col_input)
        drop_checker(board, col_index, current_player)
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} won!")
            break
        
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()