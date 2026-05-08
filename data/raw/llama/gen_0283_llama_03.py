# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 283
# filename        : gen_0283_llama_03.py
# timestamp       : 2026-04-06T09:54:55Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 390
# tokens_output   : 831
# tokens_total    : 1221
# cost_usd        : 0.000826
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
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Initialize the game board with spaces
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to print the game board
def print_board():
    os.system('clear')  # Clear the screen
    print('  A   B   C   D   E   F   G')  # Print column labels
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} | {} | {} | {} | {} | {} | {} |'.format(*row))
        print('+---+---+---+---+---+---+---+')

# Function to check if a player has won
def check_win(player):
    # Check horizontal wins
    for row in board:
        for i in range(BOARD_COLS - 3):
            if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
                return True

    # Check vertical wins
    for col in range(BOARD_COLS):
        for i in range(BOARD_ROWS - 3):
            if board[i][col] == player and board[i+1][col] == player and board[i+2][col] == player and board[i+3][col] == player:
                return True

    # Check diagonal wins (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

    return False

# Main game loop
current_player = random.randint(0, NUM_PLAYERS - 1)  # Randomly select the first player
while True:
    print_board()
    column = input("Player {}, choose a column (A-G): ".format('X' if current_player == 0 else 'O'))
    column = column.upper()  # Convert input to uppercase

    # Validate input
    while column not in 'ABCDEFG' or board[0][ord(column) - ord('A')]!= ' ':
        column = input("Invalid input. Please enter a letter between A and G: ")
        column = column.upper()

    # Drop the checker to the lowest available row in the chosen column
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][ord(column) - ord('A')] == ' ':
            board[row][ord(column) - ord('A')] = 'X' if current_player == 0 else 'O'
            break

    # Check for a win
    if check_win('X' if current_player == 0 else 'O'):
        print_board()
        print("Player {} won!".format('X' if current_player == 0 else 'O'))
        break

    # Check for a draw
    if all(board[0][col]!= ' ' for col in range(BOARD_COLS)):
        print_board()
        print("It's a draw!")
        break

    # Switch to the next player
    current_player = (current_player + 1) % NUM_PLAYERS
```