# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 232
# filename        : gen_0232_gpt4mini_12.py
# timestamp       : 2026-04-06T10:21:16Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 390
# tokens_output   : 681
# tokens_total    : 1071
# cost_usd        : 0.000467
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

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(col_input, board):
    if col_input not in 'ABCDEFG':
        return False
    col_index = ord(col_input) - ord('A')
    if board[0][col_index] != ' ':
        return False
    return True

def get_column_choice(player, board):
    while True:
        col_input = input(f"Player {PLAYER_SYMBOLS[player]}, choose a column (A-G): ").upper()
        if is_valid_input(col_input, board):
            return ord(col_input) - ord('A')
        print("Invalid input. Please try again.")

def drop_checker(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = PLAYER_SYMBOLS[player]
            return

def check_win(board, player):
    symbol = PLAYER_SYMBOLS[player]
    
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == symbol for i in range(4)):
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == symbol for i in range(4)):
                return True

    # Check diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == symbol for i in range(4)):
                return True

    # Check diagonal (down-left)
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if all(board[r + i][c - i] == symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def play_game():
    board = create_board()
    current_player = random.randint(0, 1)

    print_board(board)

    while True:
        col = get_column_choice(current_player, board)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break
        if is_draw(board):
            print("The game is a draw!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    play_game()