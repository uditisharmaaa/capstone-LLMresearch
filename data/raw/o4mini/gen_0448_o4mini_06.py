# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 448
# filename        : gen_0448_o4mini_06.py
# timestamp       : 2026-05-07T22:39:22Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 517
# tokens_total    : 907
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
board = [[" "] * COLS for _ in range(ROWS)]

def print_board():
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def drop_checker(col, checker):
    for row in reversed(board):
        if row[col] == " ":
            row[col] = checker
            return

def is_winner(checker):
    for r in range(ROWS):
        for c in range(COLS):
            if c + 3 < COLS and all(board[r][c + i] == checker for i in range(4)): return True
            if r + 3 < ROWS and all(board[r + i][c] == checker for i in range(4)): return True
            if r + 3 < ROWS and c + 3 < COLS and all(board[r + i][c + i] == checker for i in range(4)): return True
            if r + 3 < ROWS and c - 3 >= 0 and all(board[r + i][c - i] == checker for i in range(4)): return True
    return False

def is_draw():
    return all(cell != " " for row in board for cell in row)

def get_valid_column():
    while True:
        col = input("Choose a column (A-G): ").strip().upper()
        if col in "ABCDEFG" and any(row["ABCDEFG".index(col)] == " " for row in board):
            return "ABCDEFG".index(col)
        print("Invalid column. Try again.")

def connect_4():
    turn = random.randint(0, 1)
    players = ["X", "O"]
    print_board()
    while True:
        print(f"Player {players[turn]}'s turn")
        col = get_valid_column()
        drop_checker(col, players[turn])
        print_board()
        if is_winner(players[turn]):
            print(f"Player {players[turn]} won!")
            break
        if is_draw():
            print("It's a draw!")
            break
        turn = 1 - turn

connect_4()
```