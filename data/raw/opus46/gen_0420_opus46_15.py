# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 420
# filename        : gen_0420_opus46_15.py
# timestamp       : 2026-05-07T19:17:19Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 418
# tokens_output   : 1028
# tokens_total    : 1446
# cost_usd        : 0.000000
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

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(" ")
        board.append(row)
    return board

def print_board(board):
    os.system('clear')
    header = "   "
    for c in range(COLS):
        header += chr(ord('A') + c) + "   "
    print(header)
    print("+---" * COLS + "+")
    for r in range(ROWS):
        row_str = "|"
        for c in range(COLS):
            row_str += " " + board[r][c] + " |"
        print(row_str)
        print("+---" * COLS + "+")

def drop_checker(board, col, checker):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = checker
            return r
    return -1

def is_column_full(board, col):
    return board[0][col] != " "

def check_win(board, checker):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == checker and board[r][c+1] == checker and board[r][c+2] == checker and board[r][c+3] == checker:
                return True
    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == checker and board[r+1][c] == checker and board[r+2][c] == checker and board[r+3][c] == checker:
                return True
    # Diagonal down-right
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == checker and board[r+1][c+1] == checker and board[r+2][c+2] == checker and board[r+3][c+3] == checker:
                return True
    # Diagonal down-left
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if board[r][c] == checker and board[r+1][c-1] == checker and board[r+2][c-2] == checker and board[r+3][c-3] == checker:
                return True
    return False

def is_board_full(board):
    for c in range(COLS):
        if board[0][c] == " ":
            return False
    return True

def get_column(board, player):
    while True:
        choice = input("Player " + player + ", choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a letter A through G.")
            continue
        choice = choice.upper()
        if choice < 'A' or choice > 'G':
            print("Invalid input. Please enter a letter A through G.")
            continue
        col = ord(choice) - ord('A')
        if is_column_full(board, col):
            print("Column " + choice + " is full. Choose another column.")
            continue
        return col

def main():
    board = create_board()
    checkers = ["X", "O"]
    current = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        player = checkers[current]
        col = get_column(board, player)
        drop_checker(board, col, player)
        print_board(board)
        if check_win(board, player):
            print("Player " + player + " won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current = (current + 1) % NUM_PLAYERS

main()
```