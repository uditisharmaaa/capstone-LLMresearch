# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 288
# filename        : gen_0288_gemini25p_03.py
# timestamp       : 2026-05-07T17:00:23Z
# model           : @vertexai/gemini-2.5-pro
# model_short     : gemini25p
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 2996
# tokens_total    : 3371
# cost_usd        : 0.000000
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

import os
import random
import sys

# Use constant global variables for board dimensions and number of players
# This makes the code easier to modify for different board sizes or player counts.
ROWS = 6
COLS = 7
NUM_PLAYERS = 2

# Define the checkers used by the two players.
PLAYERS = ('X', 'O')

# Create a string of column labels for input validation and display.
# This dynamically adjusts if COLS is changed.
COLUMN_LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:COLS]

def clear_screen():
    """Clears the terminal screen. Uses 'cls' for Windows and 'clear' for others."""
    # This is a simple way to keep the game board clean and updated at the top of the screen.
    if os.name == 'nt': # 'nt' is the name for Windows operating systems
        os.system('cls')
    else: # For Unix-like systems (Linux, macOS)
        os.system('clear')

def create_board():
    """Creates and returns a new empty game board."""
    # The board is represented as a list of lists (a 2D array).
    # It's initialized with spaces to represent empty cells.
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the game board in a specific, formatted way."""
    # Print the column labels (A, B, C, etc.) centered over each column.
    print() # Adds a blank line for better spacing
    print('   ' + '   '.join(COLUMN_LABELS))

    # Print the top border of the board.
    print(" " + "+---" * COLS + "+")

    # Iterate through each row of the board data structure.
    for r in range(ROWS):
        # Print the contents of the row, with each cell wrapped in '|' and spaces.
        row_str = " | " + " | ".join(board[r]) + " |"
        print(row_str)
        # Print the separator line between rows.
        print(" " + "+---" * COLS + "+")
    print() # Adds a final blank line for spacing

def get_player_move(player_checker, board):
    """Prompts the current player for a move and validates it."""
    # This function will loop indefinitely until a valid move is