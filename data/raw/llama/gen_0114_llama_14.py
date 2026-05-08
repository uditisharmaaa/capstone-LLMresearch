# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 114
# filename        : gen_0114_llama_14.py
# timestamp       : 2026-04-06T09:55:52Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 660
# tokens_total    : 1050
# cost_usd        : 0.000698
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
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(' ' + cell + ' |', end='')
        print()
        print('+---+---+---+---+---+---+---+')

def check_win(board, player):
    # horizontal
    for row in board:
        for i in range(COLS - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True
    # vertical
    for col in range(COLS):
        for i in range(ROWS - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True
    # diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True
    # diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True
    return False

def game():
    board = [[' ']*COLS for _ in range(ROWS)]
    players = ['X', 'O']
    current_player = random.choice(players)
    print_board(board)
    while True:
        while True:
            col = input(f"Player {current_player}, choose a column (A-G): ").upper()
            if col < 'A' or col > 'G':
                print("Invalid input. Please enter a letter between A and G.")
                continue
            col = ord(col) - ord('A')
            if board[0][col]!= ' ':
                print("Column is full. Please choose another column.")
                continue
            for row in range(ROWS - 1, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
            break
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} won!")
            break
        if all(all(cell!= ' ' for cell in row) for row in board):
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

game()
```