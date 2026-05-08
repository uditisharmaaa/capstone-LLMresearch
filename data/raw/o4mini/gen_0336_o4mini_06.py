# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 336
# filename        : gen_0336_o4mini_06.py
# timestamp       : 2026-05-07T17:37:34Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 520
# tokens_total    : 910
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
BOARD = [[" " for _ in range(COLS)] for _ in range(ROWS)]
CHARS = "ABCDEFG"
TOKENS = ["X", "O"]

def clear_screen(): os.system('clear')

def print_board():
    clear_screen()
    print("   " + "   ".join(CHARS))
    print("+---" * COLS + "+")
    for row in BOARD:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def valid_column(col):
    return col in CHARS and BOARD[0][CHARS.index(col)] == " "

def drop_checker(col, player):
    col_idx = CHARS.index(col)
    for row in range(ROWS-1, -1, -1):
        if BOARD[row][col_idx] == " ":
            BOARD[row][col_idx] = TOKENS[player]
            return row, col_idx

def check_win(row, col, player):
    def count(dx, dy):
        r, c, count = row + dx, col + dy, 0
        while 0 <= r < ROWS and 0 <= c < COLS and BOARD[r][c] == TOKENS[player]:
            count, r, c = count + 1, r + dx, c + dy
        return count
    return any(count(dx, dy) + count(-dx, -dy) >= 3 for dx, dy in [(0,1),(1,0),(1,1),(1,-1)])

def full_board(): return all(BOARD[0][col] != " " for col in range(COLS))

def main():
    current_player = random.randint(0, PLAYERS-1)
    print_board()
    while True:
        col = input(f"Player {TOKENS[current_player]}, choose a column (A-G): ").strip().upper()
        if not valid_column(col):
            print("Invalid column. Try again.")
            continue
        row, col_idx = drop_checker(col, current_player)
        print_board()
        if check_win(row, col_idx, current_player):
            print(f"Player {TOKENS[current_player]} won!")
            break
        if full_board():
            print("It's a draw!")
            break
        current_player = 1 - current_player

if __name__ == "__main__": main()
```