# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 349
# filename        : gen_0349_sonnet46_04.py
# timestamp       : 2026-05-07T17:45:53Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1001
# tokens_total    : 1422
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
    separator = "+" + "+".join(["---"] * NUM_COLS) + "+"
    for row in board:
        print(separator)
        row_str = "|" + "|".join(f" {cell} " for cell in row) + "|"
        print(row_str)
    print(separator)


def get_player_input(board, player_index):
    checker = CHECKERS[player_index]
    while True:
        user_input = input(f"Player {checker}, choose a column (A-G): ")
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter from A to G.")
            continue
        user_input = user_input.upper()
        if user_input not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter from A to G.")
            continue
        col_index = COLUMN_LABELS.index(user_input)
        if board[0][col_index] != " ":
            print("That column is full. Please choose another column.")
            continue
        return col_index


def drop_checker(board, col_index, player_index):
    checker = CHECKERS[player_index]
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_index] == " ":
            board[row][col_index] = checker
            return row
    return -1


def check_win(board, row, col, player_index):
    checker = CHECKERS[player_index]
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]
    for row_delta, col_delta in directions:
        count = 1
        for step in range(1, 4):
            r = row + row_delta * step
            c = col + col_delta * step
            if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == checker:
                count += 1
            else:
                break
        for step in range(1, 4):
            r = row - row_delta * step
            c = col - col_delta * step
            if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == checker:
                count += 1
            else:
                break
        if count >= 4:
            return True
    return False


def check_draw(board):
    return all(board[0][col] != " " for col in range(NUM_COLS))


def play_game():
    board = initialize_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    print(f"Player {CHECKERS[current_player]} goes first!")

    while True:
        col_index = get_player_input(board, current_player)
        row_index = drop_checker(board, col_index, current_player)
        print_board(board)

        if check_win(board, row_index, col_index, current_player):
            print(f"Player {CHECKERS[current_player]} won!")
            return

        if check_draw(board):
            print("It's a draw!")
            return

        current_player = (current_player + 1) % NUM_PLAYERS


if __name__ == "__main__":
    play_game()