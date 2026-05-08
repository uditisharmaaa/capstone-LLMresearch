# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 408
# filename        : gen_0408_gemini25p_03.py
# timestamp       : 2026-05-07T19:13:57Z
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

# -- Global Constants --
# These constants define the core properties of the game.
# Using constants makes the code easier to read and modify.
# For example, to make a bigger Connect 5 game, you could change these values.

# Board dimensions
ROWS = 6
COLS = 7

# Player checkers/symbols
PLAYERS = ('X', 'O')

# Column labels for user input and board display
COL_LABELS = "ABCDEFG"

# The number of checkers in a line required to win
CONNECT_N = 4


def clear_screen():
    """
    Clears the terminal screen.
    Uses 'clear' for Unix-like systems (Linux, macOS) and 'cls' for Windows.
    """
    # The 'nt' name is used for Windows operating systems
    if os.name == 'nt':
        os.system('cls')
    # 'posix' is the name for Unix-like systems
    else:
        os.system('clear')


def create_board():
    """
    Creates an empty game board.
    The board is represented as a list of lists (a 2D grid).
    Each cell is initialized with a space character ' '.
    Returns:
        list: A 2D list representing the empty board.
    """
    # This uses a list comprehension for a concise way to build the 2D list.
    # It creates a list of ROWS number of lists, where each inner list
    # contains COLS number of space characters.
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    """
    Prints the game board in a user-friendly format.
    Includes column labels (A-G) and a grid structure.
    Args:
        board (list): The 2D list representing the current state of the board.
    """
    # Print the column headers (A, B, C, ...)
    # The ' ' * 3 creates spacing to align the letters with the columns.
    # ' '.join(...) adds a space between each letter for readability.
    print("\n   " + "   ".join(COL_LABELS))

    # Print the top border of the board
    print("+" + "---+" * COLS)

    # Iterate through each row of the board to print its contents
    for r in range(ROWS):
        # Print the checkers in the current row, separated by '|'
        # f" {board[r][c]} " ensures each checker is centered in its cell.
        row_str = "| " + " | ".join(board[r]) + " |"
        print(row_str)
