# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 267
# filename        : gen_0267_llama_02.py
# timestamp       : 2026-04-06T09:46:49Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 392
# tokens_output   : 653
# tokens_total    : 1045
# cost_usd        : 0.000694
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2

def create_board():
    return [[' ']*COLS for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} |'.format(' | '.join(row)))
        print('+---+---+---+---+---+---+---+')

def get_player_move(player):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player)).upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter from A to G.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = 'X' if player == 0 else 'O'
            return

def check_win(board, player):
    symbol = 'X' if player == 0 else 'O'
    # Check horizontal
    for row in board:
        for i in range(COLS - 3):
            if all([cell == symbol for cell in row[i:i+4]]):
                return True
    # Check vertical
    for col in range(COLS):
        for i in range(ROWS - 3):
            if all([board[row][col] == symbol for row in range(i, i+4)]):
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all([board[row+i][col+i] == symbol for i in range(4)]):
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all([board[row-i][col+i] == symbol for i in range(4)]):
                return True
    return False

def main():
    global board
    board = create_board()
    players = list(range(PLAYERS))
    random.shuffle(players)
    print("Player {} goes first.".format(players[0]))
    for player in players * (ROWS * COLS):
        print_board(board)
        col = get_player_move(player)
        drop_checker(board, col, player)
        if check_win(board, player):
            print_board(board)
            print("Player {} won!".format(player))
            return
        if all([all([cell!= ' ' for cell in row]) for row in board]):
            print_board(board)
            print("It's a draw!")
            return

if __name__ == "__main__":
    main()
```