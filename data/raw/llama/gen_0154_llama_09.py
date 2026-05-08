# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 154
# filename        : gen_0154_llama_09.py
# timestamp       : 2026-04-06T10:06:42Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

```python
import os
import random

# Constants
BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2
PLAYERS = ['X', 'O']

# Initialize the board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print()
        print('+---+---+---+---+---+---+---+')

def is_valid_input(col):
    return col.isalpha() and col.upper() in 'ABCDEFG'

def get_player_move(player):
    while True:
        col = input(f"Player {player}, choose a column (A-G): ").upper()
        if is_valid_input(col):
            col_idx = ord(col) - ord('A')
            if board[0][col_idx]!= ' ':
                print("Column is full. Choose another column.")
            else:
                return col_idx
        else:
            print("Invalid input. Please enter a letter from A to G.")

def drop_checker(player, col):
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return

def check_win(player):
    # Check horizontal locations for win
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Check vertical locations for win
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS):
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

def main():
    current_player = random.choice([0, 1])
    while True:
        print_board()
        col = get_player_move(PLAYERS[current_player])
        drop_checker(PLAYERS[current_player], col)
        if check_win(PLAYERS[current_player]):
            print_board()
            print(f"Player {PLAYERS[current_player]} won!")
            break
        if all(cell!= ' ' for row in board for cell in row):
            print_board()
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```