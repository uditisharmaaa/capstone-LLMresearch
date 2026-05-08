# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 188
# filename        : gen_0188_gpt4mini_13.py
# timestamp       : 2026-04-06T09:24:52Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 387
# tokens_output   : 637
# tokens_total    : 1024
# cost_usd        : 0.000440
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

import os
import random

ROWS = 6
COLUMNS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_ONE = 'X'
PLAYER_TWO = 'O'

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def get_player_input(player):
    while True:
        column = input(f"Player {player}, choose a column (A-G): ").upper()
        if column in "ABCDEFG":
            col_index = ord(column) - ord('A')
            if board[0][col_index] == EMPTY:
                return col_index
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid input. Please enter a letter from A to G.")

def drop_checker(board, col, player):
    for row in reversed(range(ROWS)):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return

def check_win(board, player):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal /
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    # Check diagonal \
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    return False

def check_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

board = create_board()
current_player = PLAYER_ONE if random.choice([True, False]) else PLAYER_TWO

while True:
    print_board(board)
    col = get_player_input(current_player)
    drop_checker(board, col, current_player)

    if check_win(board, current_player):
        print_board(board)
        print(f"{current_player} won!")
        break

    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    current_player = PLAYER_ONE if current_player == PLAYER_TWO else PLAYER_TWO