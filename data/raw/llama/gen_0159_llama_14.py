# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 159
# filename        : gen_0159_llama_14.py
# timestamp       : 2026-04-06T10:07:44Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 730
# tokens_total    : 1120
# cost_usd        : 0.000750
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

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

def create_board():
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    os.system('clear')
    print('  A B C D E F G')
    for row in board:
        print('+---' * NUM_COLS + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * NUM_COLS + '+')

def get_player_move(player):
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
        elif board[NUM_ROWS-1][ord(move)-65]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(move)-65

def drop_checker(board, col, player):
    for row in range(NUM_ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = 'X' if player == 0 else 'O'
            break

def check_win(board, player):
    symbol = 'X' if player == 0 else 'O'
    # Check horizontal
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS-3):
            if board[row][col] == symbol and board[row][col+1] == symbol and board[row][col+2] == symbol and board[row][col+3] == symbol:
                return True
    # Check vertical
    for row in range(NUM_ROWS-3):
        for col in range(NUM_COLS):
            if board[row][col] == symbol and board[row+1][col] == symbol and board[row+2][col] == symbol and board[row+3][col] == symbol:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(NUM_ROWS-3):
        for col in range(NUM_COLS-3):
            if board[row][col] == symbol and board[row+1][col+1] == symbol and board[row+2][col+2] == symbol and board[row+3][col+3] == symbol:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS-3):
            if board[row][col] == symbol and board[row-1][col+1] == symbol and board[row-2][col+2] == symbol and board[row-3][col+3] == symbol:
                return True
    return False

def check_draw(board):
    return all(board[row][col]!= ' ' for row in range(NUM_ROWS) for col in range(NUM_COLS))

board = create_board()
current_player = random.randint(0, 1)

while True:
    print_board(board)
    col = get_player_move(current_player)
    drop_checker(board, col, current_player)
    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} won!")
        break
    elif check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    current_player = (current_player + 1) % NUM_PLAYERS
```