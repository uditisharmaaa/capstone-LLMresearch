# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 476
# filename        : gen_0476_o4mini_04.py
# timestamp       : 2026-05-07T22:47:18Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 694
# tokens_total    : 1085
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

# Global constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def clear_screen():
    os.system('clear')

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_player_input(player):
    while True:
        column = input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a column (A-G): ").strip()
        if column in COLUMN_LABELS:
            col_index = COLUMN_LABELS.index(column)
            if not column_is_full(board, col_index):
                return col_index
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please enter a letter between A and G.")

def column_is_full(board, column):
    return all(row[column] != " " for row in board)

def drop_checker(board, column, player):
    for row in reversed(board):
        if row[column] == " ":
            row[column] = "X" if player == 1 else "O"
            break

def check_winner(board, player):
    checker = "X" if player == 1 else "O"
    for row in range(ROWS):
        for col in range(COLUMNS):
            if check_direction(board, row, col, 1, 0, checker) or \
               check_direction(board, row, col, 0, 1, checker) or \
               check_direction(board, row, col, 1, 1, checker) or \
               check_direction(board, row, col, 1, -1, checker):
                return True
    return False

def check_direction(board, row, col, row_dir, col_dir, checker):
    count = 0
    for i in range(4):
        r, c = row + i * row_dir, col + i * col_dir
        if 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == checker:
            count += 1
        else:
            break
    return count == 4

def board_is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    global board
    board = create_board()
    current_player = random.randint(1, PLAYERS)
    print_board(board)

    while True:
        print_board(board)
        col = get_player_input(current_player)
        drop_checker(board, col, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} ({'X' if current_player == 1 else 'O'}) won!")
            break

        if board_is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 3 - current_player

if __name__ == "__main__":
    main()