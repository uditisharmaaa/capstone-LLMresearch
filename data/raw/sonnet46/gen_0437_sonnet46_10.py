# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 437
# filename        : gen_0437_sonnet46_10.py
# timestamp       : 2026-05-07T22:34:55Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1150
# tokens_total    : 1569
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

import os
import random

NUM_COLS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2
CHECKERS = ["X", "O"]
COL_LABELS = "ABCDEFG"


def create_board():
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]


def print_board(board):
    os.system("clear")
    header = "   " + "   ".join(COL_LABELS)
    print(header)
    divider = "+" + "---+" * NUM_COLS
    for row in board:
        print(divider)
        row_str = "|" + "|".join(f" {cell} " for cell in row) + "|"
        print(row_str)
    print(divider)


def get_player_input(board, player):
    checker = CHECKERS[player]
    while True:
        raw = input(f"Player {checker}, choose a column (A-G): ")
        if len(raw) != 1 or not raw.isalpha():
            print("Invalid input. Please enter a single letter from A to G.")
            continue
        letter = raw.upper()
        if letter not in COL_LABELS:
            print("Invalid column. Please choose a letter from A to G.")
            continue
        col = COL_LABELS.index(letter)
        if not is_column_available(board, col):
            print("That column is full. Please choose another column.")
            continue
        return col


def is_column_available(board, col):
    return board[0][col] == " "


def drop_checker(board, col, player):
    checker = CHECKERS[player]
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = checker
            return row
    return -1


def check_horizontal(board, row, col, checker):
    count = 0
    for c in range(NUM_COLS):
        if board[row][c] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def check_vertical(board, row, col, checker):
    count = 0
    for r in range(NUM_ROWS):
        if board[r][col] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def check_diagonal_down_right(board, checker):
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if all(board[r + i][c + i] == checker for i in range(4)):
                return True
    return False


def check_diagonal_down_left(board, checker):
    for r in range(NUM_ROWS - 3):
        for c in range(3, NUM_COLS):
            if all(board[r + i][c - i] == checker for i in range(4)):
                return True
    return False


def check_win(board, row, col, player):
    checker = CHECKERS[player]
    if check_horizontal(board, row, col, checker):
        return True
    if check_vertical(board, row, col, checker):
        return True
    if check_diagonal_down_right(board, checker):
        return True
    if check_diagonal_down_left(board, checker):
        return True
    return False


def is_board_full(board):
    return all(board[0][col] != " " for col in range(NUM_COLS))


def get_starting_player():
    return random.randint(0, NUM_PLAYERS - 1)


def switch_player(current_player):
    return (current_player + 1) % NUM_PLAYERS


def play_game():
    board = create_board()
    current_player = get_starting_player()
    print_board(board)
    print(f"Player {CHECKERS[current_player]} goes first!")

    while True:
        col = get_player_input(board, current_player)
        row = drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, row, col, current_player):
            print(f"Player {CHECKERS[current_player]} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = switch_player(current_player)


play_game()