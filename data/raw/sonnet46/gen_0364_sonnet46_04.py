# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 364
# filename        : gen_0364_sonnet46_04.py
# timestamp       : 2026-05-07T17:50:06Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 914
# tokens_total    : 1335
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

import os
import random

NUM_PLAYERS = 2
NUM_COLS = 7
NUM_ROWS = 6
CHECKERS = ["X", "O"]
COLUMN_LABELS = "ABCDEFG"


def initialize_board():
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]


def print_board(board):
    os.system("clear")
    header = "   " + "   ".join(COLUMN_LABELS)
    print(header)
    separator = "+" + "---+" * NUM_COLS
    for row in board:
        print(separator)
        row_str = "|" + "|".join(f" {cell} " for cell in row) + "|"
        print(row_str)
    print(separator)


def get_player_input(player_checker):
    while True:
        raw = input(f"Player {player_checker}, choose a column (A-G): ")
        if len(raw) != 1 or not raw.isalpha():
            print("Invalid input. Please enter a single letter from A to G.")
            continue
        letter = raw.upper()
        if letter not in COLUMN_LABELS:
            print("Invalid column. Please choose a letter from A to G.")
            continue
        return COLUMN_LABELS.index(letter)


def drop_checker(board, col, checker):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = checker
            return row
    return -1


def is_column_full(board, col):
    return board[0][col] != " "


def check_winner(board, checker):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False


def is_board_full(board):
    return all(board[0][col] != " " for col in range(NUM_COLS))


def play_game():
    board = initialize_board()
    current_player_index = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        checker = CHECKERS[current_player_index]

        while True:
            col = get_player_input(checker)
            if is_column_full(board, col):
                print("That column is full. Please choose another column.")
            else:
                break

        drop_checker(board, col, checker)
        print_board(board)

        if check_winner(board, checker):
            print(f"Player {checker} won!")
            return

        if is_board_full(board):
            print("It's a draw!")
            return

        current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    play_game()