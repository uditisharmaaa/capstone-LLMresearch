# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 68
# filename        : gen_0068_gpt4o_08.py
# timestamp       : 2026-02-19T20:53:17Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 389
# tokens_output   : 684
# tokens_total    : 1073
# cost_usd        : 0.007812
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
#   Write with a focus on code readability over brevity.
# ====================================================================

import os
import random

# Global constants
BOARD_COLUMNS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2
EMPTY_SPACE = ' '
PLAYER_MARKERS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY_SPACE for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    # Print column labels
    print("   " + "   ".join(COLUMN_LABELS))
    # Print board with row separators
    for row in board:
        print("+---" * BOARD_COLUMNS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * BOARD_COLUMNS + "+")

def get_player_input(player):
    while True:
        input_col = input(f"Player {PLAYER_MARKERS[player]}, choose a column (A-G): ").strip().upper()
        if len(input_col) == 1 and input_col in COLUMN_LABELS:
            col_index = COLUMN_LABELS.index(input_col)
            if board[0][col_index] == EMPTY_SPACE:
                return col_index
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please enter a letter from A to G.")

def drop_checker(board, col, player):
    for row in reversed(board):
        if row[col] == EMPTY_SPACE:
            row[col] = PLAYER_MARKERS[player]
            return

def check_winner(board, player):
    marker = PLAYER_MARKERS[player]
    # Check horizontal
    for row in board:
        for col in range(BOARD_COLUMNS - 3):
            if all(cell == marker for cell in row[col:col+4]):
                return True
    # Check vertical
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS - 3):
            if all(board[row+i][col] == marker for i in range(4)):
                return True
    # Check diagonal /
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row+i][col+i] == marker for i in range(4)):
                return True
    # Check diagonal \
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row-i][col+i] == marker for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY_SPACE for col in range(BOARD_COLUMNS))

def main():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    
    while True:
        col = get_player_input(current_player)
        drop_checker(board, col, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {PLAYER_MARKERS[current_player]} won!")
            break
        
        if is_draw(board):
            print("The game is a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()