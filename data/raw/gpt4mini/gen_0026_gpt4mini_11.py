# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 26
# filename        : gen_0026_gpt4mini_11.py
# timestamp       : 2026-02-19T20:41:12Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 981
# tokens_total    : 1368
# cost_usd        : 0.000647
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

# Constants for board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

def create_board():
    """Create a 2D board initialized with spaces."""
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board with column labels."""
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column):
    """Check if the input column is valid (A-G)."""
    return column in "ABCDEFG"

def get_column_index(column):
    """Convert column letter to index (A=0, B=1, ..., G=6)."""
    return ord(column) - ord('A')

def is_column_full(board, col_index):
    """Check if the specified column is full."""
    return board[0][col_index] != " "

def drop_checker(board, col_index, checker):
    """Drop the checker into the lowest available row in the specified column."""
    for row in reversed(board):
        if row[col_index] == " ":
            row[col_index] = checker
            break

def check_winner(board, checker):
    """Check if the specified checker has won the game."""
    # Check horizontal, vertical, and diagonal
    return (check_horizontal(board, checker) or
            check_vertical(board, checker) or
            check_diagonal(board, checker))

def check_horizontal(board, checker):
    """Check for a horizontal win for the specified checker."""
    for row in board:
        count = 0
        for cell in row:
            count = count + 1 if cell == checker else 0
            if count == 4:
                return True
    return False

def check_vertical(board, checker):
    """Check for a vertical win for the specified checker."""
    for col in range(COLS):
        count = 0
        for row in range(ROWS):
            count = count + 1 if board[row][col] == checker else 0
            if count == 4:
                return True
    return False

def check_diagonal(board, checker):
    """Check for a diagonal win for the specified checker."""
    # Check for positive slope diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == checker and
                board[row + 1][col + 1] == checker and
                board[row + 2][col + 2] == checker and
                board[row + 3][col + 3] == checker):
                return True
    
    # Check for negative slope diagonals
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == checker and
                board[row - 1][col + 1] == checker and
                board[row - 2][col + 2] == checker and
                board[row - 3][col + 3] == checker):
                return True
                
    return False

def is_draw(board):
    """Check if the board is full and there is no winner."""
    return all(cell != " " for row in board for cell in row)

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    
    print_board(board)

    while True:
        column = input(f"Player {current_player}, choose a column (A-G): ").upper()
        if not is_valid_input(column):
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        col_index = get_column_index(column)
        if is_column_full(board, col_index):
            print("Column is full. Please choose another column.")
            continue
        
        drop_checker(board, col_index, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        
        if is_draw(board):
            print("The game is a draw!")
            break
        
        current_player = players[0] if current_player == players[1] else players[1]

if __name__ == "__main__":
    main()