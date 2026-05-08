# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 190
# filename        : gen_0190_gemini_15.py
# timestamp       : 2026-04-06T10:13:45Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 377
# tokens_output   : 1061
# tokens_total    : 1438
# cost_usd        : 0.000462
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
PLAYERS = 2
PLAYER_SYMBOLS = ["X", "O"]

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for i in range(ROWS):
        row_str = "+"
        for _ in range(COLS):
            row_str += "---+"
        print(row_str)
        row_str = "|"
        for j in range(COLS):
            row_str += " " + board[i][j] + " |"
        print(row_str)
    row_str = "+"
    for _ in range(COLS):
        row_str += "---+"
    print(row_str)

def get_player_move(player):
    while True:
        col_str = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not col_str.isalpha() or len(col_str) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = ord(col_str) - ord('A')
        if 0 <= col < COLS:
            return col
        else:
            print("Invalid column. Please enter a letter A-G.")

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = PLAYER_SYMBOLS[player]
            return row

def check_win(board, row, col, player):
    symbol = PLAYER_SYMBOLS[player]

    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == symbol:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == symbol:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == ' ':
            return False
    return True

def main():
    board = create_board()
    player = random.randint(0, PLAYERS - 1)
    game_over = False

    while not game_over:
        print_board(board)
        col = get_player_move(player)

        if not is_valid_move(board, col):
            print("Column is full. Try again.")
            continue

        row = drop_checker(board, col, player)

        if check_win(board, row, col, player):
            print_board(board)
            print(f"Player {player + 1} won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            player = (player + 1) % PLAYERS

if __name__ == "__main__":
    main()
```