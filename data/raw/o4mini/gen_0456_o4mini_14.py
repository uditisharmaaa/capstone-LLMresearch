# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 456
# filename        : gen_0456_o4mini_14.py
# timestamp       : 2026-05-07T22:42:02Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 579
# tokens_total    : 966
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

```python
import os
import random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY = " "
P1, P2 = "X", "O"
COLS_LABELS = "ABCDEFG"

def clear(): os.system('clear')

def init_board(): return [[EMPTY]*COLS for _ in range(ROWS)]

def print_board(b):
    clear()
    print("   " + "   ".join(COLS_LABELS))
    print("+" + "---+"*COLS)
    for r in b:
        print("| " + " | ".join(r) + " |")
        print("+" + "---+"*COLS)

def drop_chip(b, col, chip):
    for r in range(ROWS-1, -1, -1):
        if b[r][col] == EMPTY:
            b[r][col] = chip
            return True
    return False

def valid_col(c, b):
    return c in COLS_LABELS and any(b[r][COLS_LABELS.index(c)] == EMPTY for r in range(ROWS))

def check_win(b, chip):
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(b[r][c+i] == chip for i in range(4)): return True
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(b[r+i][c] == chip for i in range(4)): return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(b[r+i][c+i] == chip for i in range(4)): return True
    for r in range(ROWS-3):
        for c in range(3, COLS):
            if all(b[r+i][c-i] == chip for i in range(4)): return True
    return False

def full_board(b):
    return all(b[0][c] != EMPTY for c in range(COLS))

def main():
    board = init_board()
    players = [P1, P2]
    random.shuffle(players)
    print_board(board)
    while True:
        for p in players:
            while True:
                col = input(f"{p}'s turn, choose a column (A-G): ").strip().upper()
                if valid_col(col, board):
                    drop_chip(board, COLS_LABELS.index(col), p)
                    break
                print("Invalid input, try again.")
            print_board(board)
            if check_win(board, p):
                print(f"{p} won!")
                return
            if full_board(board):
                print("It's a draw!")
                return

if __name__ == "__main__":
    main()
```