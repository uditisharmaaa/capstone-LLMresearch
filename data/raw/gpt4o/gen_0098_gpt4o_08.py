# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 98
# filename        : gen_0098_gpt4o_08.py
# timestamp       : 2026-02-19T21:05:06Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 389
# tokens_output   : 847
# tokens_total    : 1236
# cost_usd        : 0.009442
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

# Constants
BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    return board[0][col] == ' '

def get_next_open_row(board, col):
    for r in range(BOARD_ROWS-1, -1, -1):
        if board[r][col] == ' ':
            return r

def drop_checker(board, row, col, checker):
    board[row][col] = checker

def check_winner(board, piece):
    # Check horizontal locations
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(3, BOARD_ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def is_draw(board):
    for c in range(BOARD_COLS):
        if is_valid_move(board, c):
            return False
    return True

def get_column_input():
    while True:
        col_input = input("Choose a column (A-G): ").strip().upper()
        if col_input in 'ABCDEFG' and len(col_input) == 1:
            return ord(col_input) - ord('A')
        print("Invalid input. Please enter a letter from A to G.")

def main():
    board = create_board()
    game_over = False
    players = ['X', 'O']
    current_player = random.randint(0, 1)

    print_board(board)
    
    while not game_over:
        print(f"Player {players[current_player]}'s turn.")
        col = get_column_input()

        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_checker(board, row, col, players[current_player])

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} won!")
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("The game is a draw!")
                game_over = True

            current_player = (current_player + 1) % NUM_PLAYERS
            print_board(board)

if __name__ == "__main__":
    main()