# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 10
# filename        : gen_0010_gpt4o_10.py
# timestamp       : 2026-02-19T20:33:28Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 390
# tokens_output   : 736
# tokens_total    : 1126
# cost_usd        : 0.008335
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
EMPTY = ' '

# Game pieces
PLAYER_PIECES = ['X', 'O']

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_column_index(column_label):
    return ord(column_label) - ord('A')

def is_valid_move(board, column):
    if column < 0 or column >= COLUMNS:
        return False
    return board[0][column] == EMPTY

def make_move(board, column, piece):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = piece
            return True
    return False

def check_winner(board, piece):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][c] == piece for c in range(col, col + 4)):
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[r][col] == piece for r in range(row, row + 4)):
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

def get_player_move():
    while True:
        move = input("Choose a column (A-G): ").strip().upper()
        if move in "ABCDEFG":
            return get_column_index(move)
        print("Invalid input. Please enter a letter from A to G.")

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)

    while True:
        print_board(board)
        print(f"Player {PLAYER_PIECES[current_player]}'s turn")
        
        column = get_player_move()
        while not is_valid_move(board, column):
            print("Column is full or invalid. Please choose another.")
            column = get_player_move()

        make_move(board, column, PLAYER_PIECES[current_player])

        if check_winner(board, PLAYER_PIECES[current_player]):
            print_board(board)
            print(f"Player {PLAYER_PIECES[current_player]} won!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()