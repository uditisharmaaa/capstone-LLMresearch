# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 235
# filename        : gen_0235_llama_15.py
# timestamp       : 2026-04-06T10:23:11Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 391
# tokens_output   : 780
# tokens_total    : 1171
# cost_usd        : 0.000788
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
#   Write in a straightforward, no-frills style.
# ====================================================================

```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
PLAYERS = ["X", "O"]

def print_board(board):
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def initialize_board():
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def is_valid_input(input_str):
    return len(input_str) == 1 and 'A' <= input_str <= 'G'

def is_valid_move(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for row in range(NUM_ROWS-1, -1, -1):
        if board[row][col] == " ":
            return row

def drop_checker(board, col, player):
    row = get_next_open_row(board, col)
    board[row][col] = player

def check_win(board, player):
    # Check horizontal locations for win
    for c in range(NUM_COLS-3):
        for r in range(NUM_ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS-3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(NUM_COLS-3):
        for r in range(NUM_ROWS-3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(NUM_COLS-3):
        for r in range(3, NUM_ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

def is_draw(board):
    for col in range(NUM_COLS):
        if board[0][col] == " ":
            return False
    return True

def main():
    board = initialize_board()
    current_player = random.choice(PLAYERS)
    while True:
        print_board(board)
        col = input(f"Player {current_player}, choose a column (A-G): ").upper()
        while not is_valid_input(col) or not is_valid_move(board, ord(col)-65):
            col = input("Invalid input. Choose a column (A-G): ").upper()
        drop_checker(board, ord(col)-65, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
```