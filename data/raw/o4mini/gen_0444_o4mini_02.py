# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 444
# filename        : gen_0444_o4mini_02.py
# timestamp       : 2026-05-07T22:36:46Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 501
# tokens_total    : 890
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

```python
import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[" "] * COLS for _ in range(ROWS)]
COL_LABELS = "ABCDEFG"
PIECES = ["X", "O"]

def clear_screen(): os.system('clear')

def print_board():
    clear_screen()
    print("   " + "   ".join(COL_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def drop_piece(col, piece):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = piece
            return r

def is_win(row, col, piece):
    def count(dx, dy):
        r, c, count = row + dx, col + dy, 0
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == piece:
            r, c, count = r + dx, c + dy, count + 1
        return count
    return any(count(dx, dy) + count(-dx, -dy) >= 3 for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)])

def is_draw(): return all(board[0][c] != " " for c in range(COLS))

def get_valid_input():
    while True:
        col = input("Choose a column (A-G): ").strip().upper()
        if col in COL_LABELS and board[0][COL_LABELS.index(col)] == " ":
            return COL_LABELS.index(col)

print_board()
current_player = random.choice(range(PLAYERS))
while True:
    print(f"Player {PIECES[current_player]}'s turn")
    col = get_valid_input()
    row = drop_piece(col, PIECES[current_player])
    print_board()
    if is_win(row, col, PIECES[current_player]):
        print(f"Player {PIECES[current_player]} won!")
        break
    if is_draw():
        print("It's a draw!")
        break
    current_player = 1 - current_player
```