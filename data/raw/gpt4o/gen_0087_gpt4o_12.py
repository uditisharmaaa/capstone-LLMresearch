# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 87
# filename        : gen_0087_gpt4o_12.py
# timestamp       : 2026-02-19T21:02:35Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 390
# tokens_output   : 694
# tokens_total    : 1084
# cost_usd        : 0.007915
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

BOARD_ROWS = 6
BOARD_COLUMNS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def initialize_board():
    return [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * BOARD_COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * BOARD_COLUMNS + "+")

def is_valid_input(input_str):
    return input_str in COLUMN_LABELS

def get_column_index(column_label):
    return COLUMN_LABELS.index(column_label)

def is_column_full(board, column):
    return board[0][column] != ' '

def make_move(board, column, symbol):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = symbol
            return

def check_winner(board, symbol):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if (check_line(board, row, col, 0, 1, symbol) or
                check_line(board, row, col, 1, 0, symbol) or
                check_line(board, row, col, 1, 1, symbol) or
                check_line(board, row, col, 1, -1, symbol)):
                return True
    return False

def check_line(board, start_row, start_col, delta_row, delta_col, symbol):
    for i in range(4):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        if not (0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLUMNS):
            return False
        if board[row][col] != symbol:
            return False
    return True

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(BOARD_COLUMNS))

def switch_player(current_player):
    return (current_player + 1) % NUM_PLAYERS

def main():
    board = initialize_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)

    while True:
        print_board(board)
        player_symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {player_symbol}'s turn")
        
        column_label = input("Choose a column (A-G): ").strip().upper()
        
        if not is_valid_input(column_label):
            print("Invalid input. Please choose a letter between A and G.")
            continue
        
        column_index = get_column_index(column_label)
        
        if is_column_full(board, column_index):
            print("Column is full. Choose another column.")
            continue
        
        make_move(board, column_index, player_symbol)
        
        if check_winner(board, player_symbol):
            print_board(board)
            print(f"Player {player_symbol} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()