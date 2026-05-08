# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 469
# filename        : gen_0469_sonnet46_12.py
# timestamp       : 2026-05-07T22:44:56Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1022
# tokens_total    : 1440
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

NUM_PLAYERS = 2
NUM_COLS = 7
NUM_ROWS = 6
PLAYERS = ["X", "O"]
COL_LABELS = "ABCDEFG"


def create_board():
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]


def print_board(board):
    os.system("clear")
    header = "   " + "   ".join(COL_LABELS)
    print(header)
    separator = "+" + "---+" * NUM_COLS
    for row in board:
        print(separator)
        row_str = "|" + "|".join(f" {cell} " for cell in row) + "|"
        print(row_str)
    print(separator)


def get_valid_input(board):
    while True:
        user_input = input("Choose a column (A-G): ")
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter between A and G.")
            continue
        user_input = user_input.upper()
        if user_input not in COL_LABELS:
            print("Invalid column. Please enter a letter between A and G.")
            continue
        col_index = COL_LABELS.index(user_input)
        if board[0][col_index] != " ":
            print("That column is full. Please choose another column.")
            continue
        return col_index


def drop_checker(board, col_index, checker):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_index] == " ":
            board[row][col_index] = checker
            return row
    return -1


def check_horizontal(board, checker):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True
    return False


def check_vertical(board, checker):
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True
    return False


def check_diagonal_down(board, checker):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True
    return False


def check_diagonal_up(board, checker):
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True
    return False


def check_win(board, checker):
    return (
        check_horizontal(board, checker)
        or check_vertical(board, checker)
        or check_diagonal_down(board, checker)
        or check_diagonal_up(board, checker)
    )


def check_draw(board):
    return all(board[0][col] != " " for col in range(NUM_COLS))


def play_game():
    board = create_board()
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)

    while True:
        current_checker = PLAYERS[current_player_index]
        print(f"Player {current_checker}'s turn.")

        col_index = get_valid_input(board)
        drop_checker(board, col_index, current_checker)
        print_board(board)

        if check_win(board, current_checker):
            print(f"Player {current_checker} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player_index = (current_player_index + 1) % NUM_PLAYERS


play_game()