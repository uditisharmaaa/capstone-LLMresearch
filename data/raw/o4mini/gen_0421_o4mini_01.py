# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 421
# filename        : gen_0421_o4mini_01.py
# timestamp       : 2026-05-07T19:17:27Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 630
# tokens_total    : 1021
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

# Global constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column, board):
    return 0 <= column < COLUMNS and board[0][column] == " "

def drop_checker(board, column, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = checker
            return row

def check_winner(board, row, column, checker):
    def count_in_direction(dx, dy):
        count = 0
        x, y = column + dx, row + dy
        while 0 <= y < ROWS and 0 <= x < COLUMNS and board[y][x] == checker:
            count += 1
            x += dx
            y += dy
        return count

    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        if 1 + count_in_direction(dx, dy) + count_in_direction(-dx, -dy) >= 4:
            return True
    return False

def is_draw(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

def get_player_input(board):
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if choice in COLUMN_LABELS:
            column = COLUMN_LABELS.index(choice)
            if is_valid_column(column, board):
                return column
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid input. Please choose a column A-G.")

def connect4():
    board = create_board()
    players = ["X", "O"]
    current_player = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)
    print(f"Player {players[current_player]} goes first!")

    while True:
        print(f"Player {players[current_player]}'s turn.")
        column = get_player_input(board)
        row = drop_checker(board, column, players[current_player])
        print_board(board)

        if check_winner(board, row, column, players[current_player]):
            print(f"Player {players[current_player]} won!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player

# Run the game
connect4()