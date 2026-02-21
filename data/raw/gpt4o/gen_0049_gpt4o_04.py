# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 49
# filename        : gen_0049_gpt4o_04.py
# timestamp       : 2026-02-19T20:46:46Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 835
# tokens_total    : 1226
# cost_usd        : 0.009327
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

ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+" + "---+" * COLUMNS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * COLUMNS)

def is_valid_input(column):
    return column in COLUMN_LABELS

def is_column_full(board, column):
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] != " "

def get_next_open_row(board, col_index):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col_index] == " ":
            return row
    return None

def drop_checker(board, row, col, piece):
    board[row][col] = piece

def check_winner(board, piece):
    # Check horizontal locations
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if (board[r][c] == piece and board[r][c+1] == piece and
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and board[r+1][c] == piece and
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if (board[r][c] == piece and board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

    return False

def is_board_full(board):
    return all(board[0][c] != " " for c in range(COLUMNS))

def main():
    board = create_board()
    game_over = False
    turn = random.randint(0, PLAYERS - 1)
    player_piece = ["X", "O"]

    while not game_over:
        print_board(board)
        print(f"Player {player_piece[turn]}'s turn")

        valid_input = False
        while not valid_input:
            column = input("Choose a column (A-G): ").upper()
            if is_valid_input(column) and not is_column_full(board, column):
                valid_input = True
            else:
                print("Invalid input. Please try again.")

        col_index = COLUMN_LABELS.index(column)
        row = get_next_open_row(board, col_index)
        drop_checker(board, row, col_index, player_piece[turn])

        if check_winner(board, player_piece[turn]):
            print_board(board)
            print(f"Player {player_piece[turn]} won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            game_over = True
        else:
            turn = (turn + 1) % PLAYERS

if __name__ == "__main__":
    main()