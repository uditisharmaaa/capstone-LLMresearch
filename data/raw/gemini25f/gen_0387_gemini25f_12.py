# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 387
# filename        : gen_0387_gemini25f_12.py
# timestamp       : 2026-05-07T17:56:51Z
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
ROWS = 6
COLUMNS = 7
PLAYERS = ('X', 'O')
EMPTY_SLOT = ' '
WIN_CONDITION = 4

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def create_board():
    """Creates and returns an empty Connect 4 board."""
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the current state of the game board."""
    # Print column labels
    print(" ", end="")
    for i in range(COLUMNS):
        print(f"  {chr(ord('A') + i)} ", end="")
    print()

    # Print top border
    print("+", end="")
    for _ in range(COLUMNS):
        print("---+", end="")
    print()

    # Print rows with checkers
    for r in range(ROWS):
        print("|", end="")
        for c in range(COLUMNS):
            print(f" {board[r][c]} |", end="")
        print()
        # Print row separator
        print("+", end="")
        for _ in range(COLUMNS):
            print("---+", end="")
        print()

def get_player_move(current_player, board):
    """
    Prompts the current player for a column choice, validates it,
    and returns the 0-indexed column number.
    """
    while True:
        col_char = input(f"Player {current_player}, choose a column (A-{chr(ord('A') + COLUMNS - 1)}): ").upper()

        if len(col_char) != 1 or not ('A' <= col_char <= chr(ord('A') + COLUMNS - 1)):
            print("Invalid input. Please enter a single letter from A to G.")
            continue

        col_index = ord(col_char) - ord('A')

        if board[0][col_index] != EMPTY_SLOT: # Check if the top slot of the column is occupied
            print("That column is full. Please choose another column.")
            continue

        return col_index

def drop_checker(board, col_index, player_char):
    """
    Drops the player's checker into the lowest available row of the chosen column.
    Modifies the board in place.
    """
    for r in range(ROWS - 1, -1, -1): # Iterate from bottom row up
        if board[r][col_index] == EMPTY_SLOT:
            board[r][col_index] = player_char
            return # Checker dropped, exit function

def check_win(board, player_char):
    """
    Checks if the given player has won the game.
    Returns True if a win is found, False otherwise.
    """
    # Check horizontal wins
    for r in range(ROWS):
        for c in range(COLUMNS - WIN_CONDITION + 1):
            if all(board[r][c + i] == player_char for i in range(WIN_CONDITION)):
                return True

    # Check vertical wins
    for c in range(COLUMNS):
        for r in range(ROWS - WIN_CONDITION + 1):
            if all(board[r + i][c] ==