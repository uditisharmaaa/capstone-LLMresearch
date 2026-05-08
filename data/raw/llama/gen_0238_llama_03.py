# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 238
# filename        : gen_0238_llama_03.py
# timestamp       : 2026-04-06T09:39:27Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 390
# tokens_output   : 830
# tokens_total    : 1220
# cost_usd        : 0.000825
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

```python
import os
import random

# Global constants for board dimensions and number of players
BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to print the board
def print_board():
    os.system('clear')  # Clear the screen
    print('  A   B   C   D   E   F   G')  # Print column labels
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end=' ')  # Print row start
        for cell in row:
            print(cell + ' | ', end='')  # Print cell and separator
        print('\n+---+---+---+---+---+---+---+')  # Print row end

# Function to handle player input
def get_player_input(player):
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").upper()
        if move not in 'ABCDEFG':  # Reject letters outside A-G
            print("Invalid input. Please enter a letter between A and G.")
        elif board[0][ord(move) - ord('A')]!= ' ':  # Reject full columns
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')  # Return column index

# Function to drop a checker into the board
def drop_checker(column, player):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = 'X' if player == 1 else 'O'  # Place checker
            return

# Function to check for a win
def check_win(player):
    # Check horizontal wins
    for row in board:
        for col in range(BOARD_COLS - 3):
            if row[col] == row[col + 1] == row[col + 2] == row[col + 3]!= ' ':
                return True
    # Check vertical wins
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]!= ' ':
                return True
    # Check diagonal wins (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]!= ' ':
                return True
    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]!= ' ':
                return True
    return False

# Main game loop
print_board()
current_player = random.randint(1, NUM_PLAYERS)  # Randomly select starting player
while True:
    print_board()
    column = get_player_input(current_player)
    drop_checker(column, current_player)
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} won!")
        break
    current_player = 2 if current_player == 1 else 1  # Switch player
    if all(cell!= ' ' for row in board for cell in row):  # Check for draw
        print_board()
        print("It's a draw!")
        break
```