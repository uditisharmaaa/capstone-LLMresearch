# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 279
# filename        : gen_0279_llama_14.py
# timestamp       : 2026-04-06T09:53:50Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 685
# tokens_total    : 1075
# cost_usd        : 0.000717
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2

# Initialize board
board = [[' ']*COLS for _ in range(ROWS)]

# Function to print the board
def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

# Function to check for a win
def check_win(player):
    # Check horizontal
    for row in board:
        for i in range(COLS-3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True

    # Check vertical
    for col in range(COLS):
        for i in range(ROWS-3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True

    return False

# Main game loop
current_player = random.randint(0, PLAYERS-1)
while True:
    print_board()
    while True:
        col = input(f"Player {['X', 'O'][current_player]}, choose a column (A-G): ").upper()
        if col < 'A' or col > 'G':
            print("Invalid column. Please choose A-G.")
        elif board[0][ord(col)-ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            break

    col = ord(col)-ord('A')
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = ['X', 'O'][current_player]
            break

    if check_win(['X', 'O'][current_player]):
        print_board()
        print(f"Player {['X', 'O'][current_player]} won!")
        break

    if all(cell!= ' ' for row in board for cell in row):
        print_board()
        print("It's a draw!")
        break

    current_player = (current_player + 1) % PLAYERS
```