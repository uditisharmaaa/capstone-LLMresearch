# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 302
# filename        : gen_0302_gemini25f_02.py
# timestamp       : 2026-05-07T17:18:09Z
# model           : @vertexai/gemini-2.5-flash
# model_short     : gemini25f
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 377
# tokens_output   : 2996
# tokens_total    : 3373
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

import os
import random
import sys

# Global Constants (Requirement 3)
BOARD_ROWS = 6
BOARD_COLS = 7
EMPTY_SLOT = ' '
PLAYERS = ['X', 'O'] # Requirement 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
WIN_LENGTH = 4 # Number of consecutive checkers for a win

def create_board():
    """Creates a 2D board initialized with spaces (Requirement 1)."""