# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 307
# filename        : gen_0307_gemini25f_07.py
# timestamp       : 2026-05-07T17:19:39Z
# model           : @vertexai/gemini-2.5-flash
# model_short     : gemini25f
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 380
# tokens_output   : 2996
# tokens_total    : 3376
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

import os
import random

# 1. Constant global variables for board dimensions and players
ROWS = 6
COLS = 7
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY_SLOT = ' '
COLUMN_LABELS = 'ABCDEFG'

def initialize_board():
    """
    Creates and returns a 2D board initialized with empty spaces.
    """
    return [[EMPTY_SLOT for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """
    Clears the screen and prints the current state of the board
    with column labels and separators.
    """
    os.system('clear') # 6. Clear the screen

    # Print column labels A-G
    print('   ' + '   '.join(COLUMN_LABELS))

    # Print the board grid
    for r in range(ROWS):
        print('+---' * COLS + '+') # Horizontal separator
        row_content = []
        for c in range(COLS):
            row_content.append(board[r][c])
        print('| ' + ' | '.join(row_content) + ' |') # Row content

    print('+---' * COLS + '+') # Final horizontal separator

def get_player_input(current_player, board):
    """
    Prompts the current player for their move, validates the input,
    and returns the chosen column index.
    Keeps asking until valid input is received