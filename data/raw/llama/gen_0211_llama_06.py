# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 211
# filename        : gen_0211_llama_06.py
# timestamp       : 2026-04-06T10:17:03Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 393
# tokens_output   : 670
# tokens_total    : 1063
# cost_usd        : 0.000707
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(' {} |'.format(cell), end='')
        print('\n+---+---+---+---+---+---+---+')

def check_win(board, player):
    # Check horizontal
    for row in board:
        for i in range(COLS - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True
    # Check vertical
    for col in range(COLS):
        for i in range(ROWS - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True
    return False

def game():
    board = [[' ']*COLS for _ in range(ROWS)]
    players = ['X', 'O']
    current_player = random.choice(players)
    while True:
        print_board(board)
        while True:
            move = input("Player {}, choose a column (A-G): ".format(current_player)).upper()
            if move < 'A' or move > 'G':
                print("Invalid input. Please enter a letter between A and G.")
            elif board[0][ord(move) - ord('A')]!= ' ':
                print("Column is full. Please choose another column.")
            else:
                break
        col = ord(move) - ord('A')
        for row in range(ROWS-1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = current_player
                break
        if check_win(board, current_player):
            print_board(board)
            print("Player {} won!".format(current_player))
            break
        if all(board[0][col]!= ' ' for col in range(COLS)):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

game()
```