# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 37
# filename        : gen_0037_gpt4o_07.py
# timestamp       : 2026-02-19T20:44:12Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 392
# tokens_output   : 774
# tokens_total    : 1166
# cost_usd        : 0.008720
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, col_index):
    return board[0][col_index] != ' '

def get_next_open_row(board, col_index):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col_index] == ' ':
            return row
    return -1

def drop_checker(board, col_index, player_symbol):
    row = get_next_open_row(board, col_index)
    if row != -1:
        board[row][col_index] = player_symbol
        return True
    return False

def check_winner(board, player_symbol):
    # Check horizontal locations for win
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player_symbol for i in range(4)):
                return True

    # Check vertical locations for win
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_symbol for i in range(4)):
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player_symbol for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player_symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    board = create_board()
    current_player = random.choice(range(PLAYERS))
    
    while True:
        print_board(board)
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn")
        
        while True:
            column_input = input("Choose a column (A-G): ").strip().upper()
            if not is_valid_column(column_input):
                print("Invalid column. Choose a letter between A and G.")
                continue

            col_index = COLUMN_LABELS.index(column_input)
            if is_column_full(board, col_index):
                print("Column is full. Choose another column.")
                continue

            if drop_checker(board, col_index, PLAYER_SYMBOLS[current_player]):
                break

        if check_winner(board, PLAYER_SYMBOLS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()