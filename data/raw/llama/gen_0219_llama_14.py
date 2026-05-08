# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 219
# filename        : gen_0219_llama_14.py
# timestamp       : 2026-04-06T10:19:02Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 753
# tokens_total    : 1143
# cost_usd        : 0.000768
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

ROWS = 6
COLS = 7
PLAYERS = 2

def print_board(board):
    os.system('clear')
    print('  A B C D E F G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

def is_valid_move(board, col):
    return board[0][col] == ' '

def get_move(player):
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid column. Try again.")
        elif not is_valid_move(board, ord(move) - 65):
            print("Column is full. Try again.")
        else:
            return ord(move) - 65

def make_move(board, player, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = 'X' if player == 0 else 'O'
            break

def check_win(board, player):
    symbol = 'X' if player == 0 else 'O'
    # Check horizontal locations for win
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == symbol and board[r][c + 1] == symbol and board[r][c + 2] == symbol and board[r][c + 3] == symbol:
                return True
    # Check vertical locations for win
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == symbol and board[r + 1][c] == symbol and board[r + 2][c] == symbol and board[r + 3][c] == symbol:
                return True
    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == symbol and board[r + 1][c + 1] == symbol and board[r + 2][c + 2] == symbol and board[r + 3][c + 3] == symbol:
                return True
    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == symbol and board[r - 1][c + 1] == symbol and board[r - 2][c + 2] == symbol and board[r - 3][c + 3] == symbol:
                return True

board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = [0, 1]
current_player = random.choice(players)
print_board(board)

while True:
    col = get_move(current_player)
    make_move(board, current_player, col)
    print_board(board)
    if check_win(board, current_player):
        print(f"Player {current_player} won!")
        break
    if all([board[0][c]!= ' ' for c in range(COLS)]):
        print("It's a draw!")
        break
    current_player = 1 - current_player
```