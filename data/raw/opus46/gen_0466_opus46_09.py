# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 466
# filename        : gen_0466_opus46_09.py
# timestamp       : 2026-05-07T22:44:10Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 420
# tokens_output   : 1168
# tokens_total    : 1588
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================



```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for r in range(NUM_ROWS):
        row = []
        for c in range(NUM_COLS):
            row.append(" ")
        board.append(row)
    return board

def print_board(board):
    os.system('clear')
    header = "   "
    for c in range(NUM_COLS):
        letter = chr(ord('A') + c)
        header = header + letter + "   "
    print(header)
    for r in range(NUM_ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for c in range(NUM_COLS):
            row_str = row_str + " " + board[r][c] + " |"
        print(row_str)
    print("+---+---+---+---+---+---+---+")

def drop_checker(board, col, checker):
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = checker
            return r
    return -1

def is_column_full(board, col):
    return board[0][col] != " "

def is_board_full(board):
    for c in range(NUM_COLS):
        if board[0][c] == " ":
            return False
    return True

def check_win(board, checker):
    # Check horizontal
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if board[r][c] == checker and board[r][c+1] == checker and board[r][c+2] == checker and board[r][c+3] == checker:
                return True

    # Check vertical
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS):
            if board[r][c] == checker and board[r+1][c] == checker and board[r+2][c] == checker and board[r+3][c] == checker:
                return True

    # Check diagonal (top-left to bottom-right)
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if board[r][c] == checker and board[r+1][c+1] == checker and board[r+2][c+2] == checker and board[r+3][c+3] == checker:
                return True

    # Check diagonal (bottom-left to top-right)
    for r in range(3, NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if board[r][c] == checker and board[r-1][c+1] == checker and board[r-2][c+2] == checker and board[r-3][c+3] == checker:
                return True

    return False

def get_column_input(board, player_checker):
    valid_letters = []
    for i in range(NUM_COLS):
        valid_letters.append(chr(ord('A') + i))

    while True:
        choice = input("Player " + player_checker + ", choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        choice = choice.upper()
        if choice not in valid_letters:
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
    current_player = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    game_over = False
    while not game_over:
        checker = checkers[current_player]
        col = get_column_input(board, checker)
        drop_checker(board, col, checker)
        print_board(board)

        if check_win(board, checker):
            print("Player " + checker + " won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

main()
```