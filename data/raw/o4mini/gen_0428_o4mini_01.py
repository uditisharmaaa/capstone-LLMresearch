# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 428
# filename        : gen_0428_o4mini_01.py
# timestamp       : 2026-05-07T22:32:14Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 735
# tokens_total    : 1126
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
PLAYERS = 2
EMPTY_SPACE = ' '
PLAYER_MARKERS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[EMPTY_SPACE for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, column_index):
    return board[0][column_index] != EMPTY_SPACE

def get_column_index(column):
    return COLUMN_LABELS.index(column)

def drop_checker(board, column_index, marker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column_index] == EMPTY_SPACE:
            board[row][column_index] = marker
            return

def check_winner(board, marker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == marker for i in range(4)):
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == marker for i in range(4)):
                return True
    # Check diagonals (down-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == marker for i in range(4)):
                return True
    # Check diagonals (down-left)
    for row in range(ROWS - 3):
        for col in range(3, COLUMNS):
            if all(board[row + i][col - i] == marker for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY_SPACE for col in range(COLUMNS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    
    print_board(board)
    while True:
        print(f"Player {PLAYER_MARKERS[current_player]}'s turn")
        
        while True:
            column = input("Choose a column (A-G): ").strip().upper()
            if not is_valid_column(column):
                print("Invalid input. Please choose a column between A and G.")
                continue
            column_index = get_column_index(column)
            if is_column_full(board, column_index):
                print("Column is full. Please choose a different column.")
                continue
            break
        
        drop_checker(board, column_index, PLAYER_MARKERS[current_player])
        print_board(board)
        
        if check_winner(board, PLAYER_MARKERS[current_player]):
            print(f"Player {PLAYER_MARKERS[current_player]} won!")
            break
        if is_board_full(board):
            print("The game is a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()