# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 318
# filename        : gen_0318_gemini25p_03.py
# timestamp       : 2026-05-07T17:31:53Z
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

# --- Global Constants ---
# These constants define the game's parameters and can be easily changed.
# ROWS: The number of rows on the game board.
# COLS: The number of columns on the game board.
# PLAYERS: A tuple containing the characters representing each player.
# CONNECT_LENGTH: The number of checkers in a line required to win.
ROWS = 6
COLS = 7
PLAYERS = ('X', 'O')
CONNECT_LENGTH = 4

def