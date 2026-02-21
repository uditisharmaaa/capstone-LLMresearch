# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 71
# filename        : gen_0071_gpt4o_11.py
# timestamp       : 2026-02-19T20:59:34Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 717
# tokens_total    : 1104
# cost_usd        : 0.008138
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
#   Write with extensive docstrings for every function.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2

def clear_screen():
    """Clear the console screen."""
    os.system('clear')

def initialize_board():
    """Create and return an empty Connect 4 board."""
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def get_move(player):
    """Prompt the player for a valid column move."""
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").upper()
        if move in "ABCDEFG":
            return ord(move) - ord('A')
        print("Invalid input. Please enter a letter between A and G.")

def is_valid_move(board, col):
    """Check if the move can be made in the specified column."""
    return board[0][col] == ' '

def make_move(board, col, checker):
    """Place the player's checker in the lowest available position in the column."""
    for row in reversed(range(ROWS)):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row, col

def check_winner(board, row, col, checker):
    """Check if the current move resulted in a win."""
    def count_consecutive(delta_row, delta_col):
        count = 0
        r, c = row, col
        while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == checker:
            count += 1
            r += delta_row
            c += delta_col
        return count

    # Horizontal, vertical, and both diagonal checks
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        if count_consecutive(dr, dc) + count_consecutive(-dr, -dc) - 1 >= 4:
            return True
    return False

def board_full(board):
    """Check if the board is completely filled."""
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def main():
    """Run the Connect 4 game."""
    board = initialize_board()
    current_player = random.choice(['X', 'O'])
    print_board(board)

    while True:
        col = get_move(current_player)
        while not is_valid_move(board, col):
            print("Column is full. Choose another column.")
            col = get_move(current_player)

        row, col = make_move(board, col, current_player)
        print_board(board)

        if check_winner(board, row, col, current_player):
            print(f"Player {current_player} won!")
            break

        if board_full(board):
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()