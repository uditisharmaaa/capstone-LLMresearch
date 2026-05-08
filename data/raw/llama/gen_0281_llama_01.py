# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 281
# filename        : gen_0281_llama_01.py
# timestamp       : 2026-04-06T09:54:25Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 394
# tokens_output   : 803
# tokens_total    : 1197
# cost_usd        : 0.000807
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

```python
import os
import random

# Constants
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Initialize the board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Define the players
players = ['X', 'O']

# Randomly select the first player
current_player = random.choice(players)

def print_board():
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
        print('+---+---+---+---+---+---+---+')
    print()

def is_valid_move(col):
    return col in 'ABCDEFG' and board[0][ord(col) - ord('A')] == ' '

def get_next_open_row(col):
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][ord(col) - ord('A')] == ' ':
            return row

def winning_move(player):
    # Check horizontal locations for win
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Check vertical locations for win
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Check positively sloped diagonals
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # Check negatively sloped diagonals
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

def game_over():
    if winning_move(players[0]):
        print_board()
        print(f"Player {players[0]} won!")
        return True
    elif winning_move(players[1]):
        print_board()
        print(f"Player {players[1]} won!")
        return True
    elif all(cell!= ' ' for row in board for cell in row):
        print_board()
        print("It's a draw!")
        return True
    return False

while True:
    print_board()
    move = input(f"Player {current_player}, choose a column (A-G): ").upper()
    while not is_valid_move(move):
        move = input(f"Invalid move, Player {current_player}. Choose a column (A-G): ").upper()
    row = get_next_open_row(move)
    board[row][ord(move) - ord('A')] = current_player
    if game_over():
        break
    current_player = players[(players.index(current_player) + 1) % NUM_PLAYERS]
```