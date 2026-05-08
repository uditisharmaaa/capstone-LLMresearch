# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 199
# filename        : gen_0199_llama_09.py
# timestamp       : 2026-04-06T10:14:57Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 394
# tokens_output   : 756
# tokens_total    : 1150
# cost_usd        : 0.000772
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

```python
import os
import random

# Global constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Function to print the board
def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
        print('+---+---+---+---+---+---+---+')
    print()

# Function to check for a win
def check_win(player):
    # Check horizontal wins
    for row in board:
        for i in range(BOARD_WIDTH - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True

    # Check vertical wins
    for col in range(BOARD_WIDTH):
        for i in range(BOARD_HEIGHT - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True

    # Check diagonal wins (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True

    return False

# Randomly select the first player
current_player = random.randint(0, NUM_PLAYERS - 1)

# Main game loop
while True:
    print_board()
    player_checker = 'X' if current_player == 0 else 'O'

    # Get the player's move
    while True:
        move = input(f"Player {player_checker}, choose a column (A-G): ")
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = ord(move) - ord('A')
        if board[0][col]!= ' ':
            print("Column is full. Please choose another column.")
            continue
        break

    # Drop the checker to the lowest available row
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player_checker
            break

    # Check for a win
    if check_win(player_checker):
        print_board()
        print(f"Player {player_checker} won!")
        break

    # Check for a draw
    if all(cell!= ' ' for row in board for cell in row):
        print_board()
        print("It's a draw!")
        break

    # Switch players
    current_player = (current_player + 1) % NUM_PLAYERS
```