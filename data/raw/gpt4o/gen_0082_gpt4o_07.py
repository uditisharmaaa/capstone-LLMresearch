# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 82
# filename        : gen_0082_gpt4o_07.py
# timestamp       : 2026-02-19T21:01:35Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 392
# tokens_output   : 697
# tokens_total    : 1089
# cost_usd        : 0.007950
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

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, column):
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] != ' '

def drop_checker(board, column, symbol):
    col_index = COLUMN_LABELS.index(column)
    for row in reversed(board):
        if row[col_index] == ' ':
            row[col_index] = symbol
            break

def check_winner(board, symbol):
    # Check horizontal locations
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == symbol for i in range(4)):
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == symbol for i in range(4)):
                return True

    # Check positively sloped diagonals
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == symbol for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLUMNS))

def connect_four():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    game_over = False

    print_board(board)

    while not game_over:
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn")
        column = input("Choose a column (A-G): ").strip().upper()

        if not is_valid_column(column):
            print("Invalid input. Please choose a letter from A to G.")
            continue

        if is_column_full(board, column):
            print("Column is full. Please choose another column.")
            continue

        drop_checker(board, column, PLAYER_SYMBOLS[current_player])
        print_board(board)

        if check_winner(board, PLAYER_SYMBOLS[current_player]):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            game_over = True
        elif is_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS

connect_four()