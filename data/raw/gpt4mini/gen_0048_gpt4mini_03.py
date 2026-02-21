# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 48
# filename        : gen_0048_gpt4mini_03.py
# timestamp       : 2026-02-19T20:46:35Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 840
# tokens_total    : 1227
# cost_usd        : 0.000562
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

import os
import random

# Constants for the board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

# Initialize the board as a 2D list filled with spaces
def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Print the current state of the board
def print_board(board):
    os.system('clear')  # Clear the screen
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print('|' + '|'.join(row) + '|')
        print("+---+---+---+---+---+---+---+")

# Check if the specified column is valid
def is_valid_column(board, col):
    return 0 <= col < COLS and board[0][col] == ' '

# Get the next available row in the specified column
def get_next_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            return row
    return -1

# Check for a win condition
def check_win(board, player):
    # Check horizontal, vertical, and diagonal wins
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False

# Check if the board is full
def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

# Main game function
def connect_four():
    board = create_board()  # Create a new game board
    current_player = random.choice(['X', 'O'])  # Randomly select the first player
    print(f"Player {current_player} goes first!")

    while True:
        print_board(board)  # Print the current board
        # Get valid column input from the current player
        while True:
            choice = input(f"Player {current_player}, choose a column (A-G): ").upper()
            if len(choice) == 1 and choice in "ABCDEFG":
                col = ord(choice) - ord('A')  # Convert letter to column index
                if is_valid_column(board, col):
                    break
                else:
                    print("Column is full, choose another column.")
            else:
                print("Invalid input, please enter a letter from A to G.")

        # Drop the checker into the chosen column
        row = get_next_row(board, col)
        board[row][col] = current_player

        # Check for win or draw after the move
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")  # Announce the winner
            break
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")  # Announce draw if the board is full
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    connect_four()  # Run the game function