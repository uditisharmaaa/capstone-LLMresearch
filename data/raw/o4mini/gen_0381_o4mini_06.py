# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 381
# filename        : gen_0381_o4mini_06.py
# timestamp       : 2026-05-07T17:55:04Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 539
# tokens_total    : 929
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

```python
import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, X, O = ' ', 'X', 'O'
COL_LABELS = 'ABCDEFG'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COL_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def drop_checker(board, col, checker):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = checker
            return row, col

def is_valid_column(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY

def check_win(board, row, col, checker):
    def count(dx, dy):
        r, c, cnt = row + dx, col + dy, 0
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            cnt, r, c = cnt + 1, r + dx, c + dy
        return cnt

    return any(count(dx, dy) + count(-dx, -dy) >= 3 for dx, dy in [(0,1), (1,0), (1,1), (1,-1)])

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = create_board()
    players = [X, O]
    random.shuffle(players)
    print_board(board)

    while True:
        for player in players:
            while True:
                col = input(f"Player {player}, choose a column (A-G): ").strip()
                if len(col) == 1 and col in COL_LABELS:
                    col_idx = COL_LABELS.index(col)
                    if is_valid_column(board, col_idx):
                        break
                print("Invalid input. Try again.")
            row, col = drop_checker(board, col_idx, player)
            print_board(board)
            if check_win(board, row, col, player):
                print(f"Player {player} won!")
                return
            if is_draw(board):
                print("It's a draw!")
                return

main()
```