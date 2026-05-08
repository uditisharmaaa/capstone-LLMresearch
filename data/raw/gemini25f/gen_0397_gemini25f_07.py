# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 397
# filename        : gen_0397_gemini25f_07.py
# timestamp       : 2026-05-07T18:01:46Z
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

# 1. Global constants for board dimensions and player symbols
ROWS = 6
COLS = 7
EMPTY_SPACE = ' '
PLAYERS = ['X', 'O']

# Helper function to convert a column letter (A-G) to its numerical index (0-6)
def column_to_index(col_letter):
    return ord(col_letter.upper()) - ord('A')

# Helper function to convert a column index (0-6) to its letter (