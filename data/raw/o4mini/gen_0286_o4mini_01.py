# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 286
# filename        : gen_0286_o4mini_01.py
# timestamp       : 2026-05-07T16:59:32Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 665
# tokens_total    : 1056
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

# Constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
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

def get_column_input(player):
    while True:
        column_input = input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a column (A-G): ").strip().upper()
        if column_input in COLUMN_LABELS:
            column_index = COLUMN_LABELS.index(column_input)
            if board[0][column_index] == ' ':
                return column_index
            else:
                print("That column is full. Choose another.")
        else:
            print("Invalid input. Please choose a column between A and G.")

def drop_checker(board, column, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = checker
            return

def check_winner(board, checker):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if col + 3 < COLUMNS and all(board[row][col + i] == checker for i in range(4)):
                return True
            if row + 3 < ROWS and all(board[row + i][col] == checker for i in range(4)):
                return True
            if row + 3 < ROWS and col + 3 < COLUMNS and all(board[row + i][col + i] == checker for i in range(4)):
                return True
            if row + 3 < ROWS and col - 3 >= 0 and all(board[row + i][col - i] == checker for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def main():
    global board
    board = create_board()
    players = [1, 2]
    current_player = random.choice(players)
    print_board(board)

    while True:
        print_board(board)
        column = get_column_input(current_player)
        checker = 'X' if current_player == 1 else 'O'
        drop_checker(board, column, checker)

        if check_winner(board, checker):
            print_board(board)
            print(f"Player {current_player} ({checker}) won!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 1 if current_player == 2 else 2

if __name__ == "__main__":
    main()