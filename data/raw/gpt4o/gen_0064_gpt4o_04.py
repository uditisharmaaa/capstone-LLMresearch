# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 64
# filename        : gen_0064_gpt4o_04.py
# timestamp       : 2026-02-19T20:52:24Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 737
# tokens_total    : 1128
# cost_usd        : 0.008348
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
EMPTY = ' '
PLAYER_TOKENS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+" + "---+" * COLUMNS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * COLUMNS)

def is_valid_column(column):
    return column in COLUMN_LABELS

def get_column_index(column):
    return COLUMN_LABELS.index(column)

def is_column_full(board, column_index):
    return board[0][column_index] != EMPTY

def drop_checker(board, column_index, token):
    for row in reversed(board):
        if row[column_index] == EMPTY:
            row[column_index] = token
            return

def check_line_winner(line, token):
    count = 0
    for cell in line:
        if cell == token:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_winner(board, token):
    # Check horizontal
    for row in board:
        if check_line_winner(row, token):
            return True

    # Check vertical
    for col in range(COLUMNS):
        column = [board[row][col] for row in range(ROWS)]
        if check_line_winner(column, token):
            return True

    # Check diagonals
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == token for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == token for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_player_input():
    while True:
        column = input("Choose a column (A-G): ").strip().upper()
        if is_valid_column(column):
            return column
        print("Invalid input. Please enter a letter from A to G.")

def play_game():
    board = create_board()
    current_player = random.choice([0, 1])
    
    while True:
        print_board(board)
        print(f"Player {PLAYER_TOKENS[current_player]}'s turn.")
        
        while True:
            column = get_player_input()
            column_index = get_column_index(column)
            if not is_column_full(board, column_index):
                break
            print("Column is full. Choose another one.")
        
        drop_checker(board, column_index, PLAYER_TOKENS[current_player])
        
        if check_winner(board, PLAYER_TOKENS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_TOKENS[current_player]} won!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()