# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 224
# filename        : gen_0224_gpt4mini_04.py
# timestamp       : 2026-04-06T09:34:02Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 391
# tokens_output   : 721
# tokens_total    : 1112
# cost_usd        : 0.000491
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
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column, board):
    if column not in 'ABCDEFG':
        return False
    col_index = ord(column) - ord('A')
    return 0 <= col_index < COLS and board[0][col_index] == ' '

def drop_checker(board, column, player):
    col_index = ord(column) - ord('A')
    for row in reversed(range(ROWS)):
        if board[row][col_index] == ' ':
            board[row][col_index] = PLAYER_SYMBOLS[player]
            return True
    return False

def check_winner(board, player):
    symbol = PLAYER_SYMBOLS[player]
    
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == symbol for i in range(4)):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == symbol for i in range(4)):
                return True

    # Check diagonal (bottom left to top right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == symbol for i in range(4)):
                return True

    # Check diagonal (top left to bottom right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)

    while True:
        print_board(board)
        column = input(f"Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").upper()

        while not is_valid_input(column, board):
            print("Invalid input. Please choose a valid column (A-G) that is not full.")
            column = input(f"Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").upper()

        drop_checker(board, column, current_player)

        if check_winner(board, current_player):
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