# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 174
# filename        : gen_0174_llama_14.py
# timestamp       : 2026-04-06T10:10:57Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 715
# tokens_total    : 1105
# cost_usd        : 0.000739
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

ROWS, COLS, PLAYERS = 6, 7, 2

board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']
current_player = random.randint(0, PLAYERS - 1)

def print_board():
    os.system('clear')
    print('  A B C D E F G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---+---+---+---+---+---+---+')

def is_valid_move(col):
    return col in 'ABCDEFG' and board[0][ord(col) - 65] == ' '

def get_next_open_row(col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][ord(col) - 65] == ' ':
            return row

def winning_move():
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == players[current_player] and board[r][c + 1] == players[current_player] and board[r][c + 2] == players[current_player] and board[r][c + 3] == players[current_player]:
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == players[current_player] and board[r + 1][c] == players[current_player] and board[r + 2][c] == players[current_player] and board[r + 3][c] == players[current_player]:
                return True

    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == players[current_player] and board[r + 1][c + 1] == players[current_player] and board[r + 2][c + 2] == players[current_player] and board[r + 3][c + 3] == players[current_player]:
                return True

    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == players[current_player] and board[r - 1][c + 1] == players[current_player] and board[r - 2][c + 2] == players[current_player] and board[r - 3][c + 3] == players[current_player]:
                return True

def game_over():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

while True:
    print_board()
    move = input(f"Player {players[current_player]}, choose a column: ")
    while not is_valid_move(move):
        move = input("Invalid move, choose a column: ")
    row = get_next_open_row(move)
    board[row][ord(move) - 65] = players[current_player]
    if winning_move():
        print_board()
        print(f"Player {players[current_player]} won!")
        break
    if game_over():
        print_board()
        print("It's a draw!")
        break
    current_player = (current_player + 1) % PLAYERS
```