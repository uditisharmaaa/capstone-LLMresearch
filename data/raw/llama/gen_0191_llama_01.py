# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 191
# filename        : gen_0191_llama_01.py
# timestamp       : 2026-04-06T09:25:45Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 394
# tokens_output   : 796
# tokens_total    : 1190
# cost_usd        : 0.000802
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
PLAYER_CHECKERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---+---+---+---+---+---+---+')

def is_valid_input(column):
    return column.isalpha() and 'A' <= column <= 'G'

def is_valid_move(board, column):
    return board[0][ord(column) - ord('A')] == ' '

def get_player_move(player):
    while True:
        column = input(f"Player {player}, choose a column (A-G): ").upper()
        if is_valid_input(column) and is_valid_move(board, column):
            return ord(column) - ord('A')

def drop_checker(board, column, player):
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = PLAYER_CHECKERS[player]
            return

def check_win(board, player):
    checker = PLAYER_CHECKERS[player]
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == checker and board[row][col + 1] == checker and board[row][col + 2] == checker and board[row][col + 3] == checker:
                return True
    # Check vertical
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS):
            if board[row][col] == checker and board[row + 1][col] == checker and board[row + 2][col] == checker and board[row + 3][col] == checker:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == checker and board[row + 1][col + 1] == checker and board[row + 2][col + 2] == checker and board[row + 3][col + 3] == checker:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == checker and board[row - 1][col + 1] == checker and board[row - 2][col + 2] == checker and board[row - 3][col + 3] == checker:
                return True
    return False

def is_draw(board):
    return all([cell!= ' ' for row in board for cell in row])

board = create_board()
print_board(board)
current_player = random.randint(0, NUM_PLAYERS - 1)

while True:
    print_board(board)
    column = get_player_move(current_player)
    drop_checker(board, column, current_player)
    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player + 1} won!")
        break
    elif is_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    current_player = (current_player + 1) % NUM_PLAYERS
```