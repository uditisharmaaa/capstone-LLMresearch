# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 126
# filename        : gen_0126_gpt4mini_11.py
# timestamp       : 2026-04-06T09:06:16Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 758
# tokens_total    : 1145
# cost_usd        : 0.000513
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

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Creates a 2D board initialized with spaces."""
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the current state of the board."""
    os.system('clear')  # Clear the screen
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---+" + "---+".join([''] * COLS))
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+" + "---+".join([''] * COLS))

def is_valid_input(column):
    """Validates the input column to ensure it's within A-G and the column is not full."""
    if column not in COLUMN_LABELS:
        return False
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] == ' '

def drop_checker(board, column, player):
    """Drops the player's checker into the chosen column."""
    col_index = COLUMN_LABELS.index(column)
    for row in reversed(range(ROWS)):
        if board[row][col_index] == ' ':
            board[row][col_index] = PLAYER_SYMBOLS[player]
            return True
    return False

def check_winner(board):
    """Checks for a winner on the board."""
    # Check horizontal, vertical, and diagonal (both directions)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == ' ':
                continue
            if c + 3 < COLS and all(board[r][c + i] == board[r][c] for i in range(4)):
                return True
            if r + 3 < ROWS:
                if all(board[r + i][c] == board[r][c] for i in range(4)):
                    return True
                if c + 3 < COLS and all(board[r + i][c + i] == board[r][c] for i in range(4)):
                    return True
                if c - 3 >= 0 and all(board[r + i][c - i] == board[r][c] for i in range(4)):
                    return True
    return False

def is_draw(board):
    """Checks if the board is full with no winner."""
    return all(board[0][c] != ' ' for c in range(COLS))

def main():
    """Main function to run the Connect 4 game."""
    global board
    board = create_board()
    current_player = random.randint(0, 1)
    
    print_board(board)
    
    while True:
        column = input(f"Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").upper()
        
        while not is_valid_input(column):
            column = input(f"Invalid input. Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").upper()
        
        drop_checker(board, column, current_player)
        print_board(board)
        
        if check_winner(board):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break
        
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()