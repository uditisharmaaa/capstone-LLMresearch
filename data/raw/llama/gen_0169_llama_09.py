# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 169
# filename        : gen_0169_llama_09.py
# timestamp       : 2026-04-06T10:09:47Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 394
# tokens_output   : 724
# tokens_total    : 1118
# cost_usd        : 0.000748
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

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Initialize the board
board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Function to print the board
def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(' ' + cell + ' |', end='')
        print()
        print('+---+---+---+---+---+---+---+')

# Function to handle player move
def player_move(player, column):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player
            return

# Function to check for win
def check_win(player):
    # Check horizontal
    for row in board:
        for i in range(BOARD_WIDTH - 3):
            if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
                return True

    # Check vertical
    for col in range(BOARD_WIDTH):
        for i in range(BOARD_HEIGHT - 3):
            if board[i][col] == player and board[i+1][col] == player and board[i+2][col] == player and board[i+3][col] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

    return False

# Main game loop
players = ['X', 'O']
current_player = random.choice(players)
while True:
    print_board()
    while True:
        column = input("Player " + current_player + ", choose a column (A-G): ").upper()
        if column < 'A' or column > 'G':
            print("Invalid column. Please choose a column between A and G.")
        elif board[0][ord(column) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            player_move(current_player, ord(column) - ord('A'))
            break

    if check_win(current_player):
        print_board()
        print("Player " + current_player + " won!")
        break

    if all(all(cell!= ' ' for cell in row) for row in board):
        print_board()
        print("It's a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
```