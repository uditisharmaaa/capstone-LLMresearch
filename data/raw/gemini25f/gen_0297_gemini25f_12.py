# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 297
# filename        : gen_0297_gemini25f_12.py
# timestamp       : 2026-05-07T17:02:56Z
# model           : @vertexai/gemini-2.5-flash
# model_short     : gemini25f
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 378
# tokens_output   : 2996
# tokens_total    : 3374
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

import os
import random

# Global Constants
NUM_ROWS = 6
NUM_COLS = 7
EMPTY_CELL = ' '
PLAYERS = ('X', 'O')
COLUMN_LABELS = tuple(chr(ord('A') + i) for i in range(NUM_COLS))

def create_board():
    """
    Initializes a 2D board with NUM_ROWS rows and NUM_COLS columns,
    filled with EMPTY_CELL characters.
    """
    return [[EMPTY_CELL for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """
    Clears the screen and prints the current state of the board
    with column labels and proper formatting.
    """
    os.system('clear')

    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))

    # Print board rows
    for r in range(NUM_ROWS):
        print('+---' * NUM_COLS + '+')
        row_str = '|'
        for c in range(NUM_COLS):
            row_str += f' {board[r][c]} |'
        print(row_str)
    print('+---' * NUM_COLS + '+') # Bottom border

def is_valid_column(col_input):
    """
    Checks if the given column input is a valid column label (A-G).
    Returns the column index (0-6) if valid, otherwise None.
    """
    if not isinstance(col_input, str) or len(col_input) != 1 or not col_input.isalpha():
        return None
    
    col_input = col_input.upper