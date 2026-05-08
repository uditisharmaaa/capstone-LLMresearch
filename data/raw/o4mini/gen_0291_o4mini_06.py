# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 291
# filename        : gen_0291_o4mini_06.py
# timestamp       : 2026-05-07T17:01:00Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 549
# tokens_total    : 939
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
import os
import random

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[" "] * COLS for _ in range(ROWS)]
COL_LABELS = "ABCDEFG"
PLAYER_SYMBOLS = ["X", "O"]

def print_board():
    os.system('clear')
    print("   " + "   ".join(COL_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def get_column():
    while True:
        col = input("Choose a column (A-G): ").strip()
        if col in COL_LABELS:
            idx = COL_LABELS.index(col)
            if board[0][idx] == " ":
                return idx
            else:
                print("Column is full!")
        else:
            print("Invalid input!")

def drop_checker(col, symbol):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = symbol
            return row

def check_winner(row, col, symbol):
    def count(dx, dy):
        r, c, total = row + dx, col + dy, 0
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == symbol:
            total, r, c = total + 1, r + dx, c + dy
        return total
    return any(count(dx, dy) + count(-dx, -dy) + 1 >= 4 for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)])

def is_draw(): return all(board[0][c] != " " for c in range(COLS))

def main():
    current_player = random.randint(0, PLAYERS - 1)
    print_board()
    while True:
        print(f"Player {current_player + 1} ({PLAYER_SYMBOLS[current_player]})'s turn")
        col = get_column()
        row = drop_checker(col, PLAYER_SYMBOLS[current_player])
        print_board()
        if check_winner(row, col, PLAYER_SYMBOLS[current_player]):
            print(f"Player {current_player + 1} won!")
            break
        if is_draw():
            print("It's a draw!")
            break
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
```