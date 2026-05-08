# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 234
# filename        : gen_0234_gemini_14.py
# timestamp       : 2026-04-06T10:21:40Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 375
# tokens_output   : 1030
# tokens_total    : 1405
# cost_usd        : 0.000450
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

ROWS = 6
COLS = 7
PLAYERS = 2
P1 = "X"
P2 = "O"

def create_board():
    b = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    return b

def print_board(b):
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for r in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for c in range(COLS):
            print(" " + b[r][c] + " |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_player_move(b, player):
    while True:
        col_str = input(f"Player {player}, enter column (A-G): ").upper()
        if not col_str.isalpha() or len(col_str) != 1:
            print("Invalid input. Enter a letter A-G.")
            continue
        col = ord(col_str) - ord('A')
        if not (0 <= col < COLS):
            print("Invalid column. Choose a column A-G.")
            continue
        if b[0][col] != " ":
            print("Column is full. Choose another column.")
            continue
        return col

def drop_checker(b, col, player):
    for r in range(ROWS - 1, -1, -1):
        if b[r][col] == " ":
            b[r][col] = player
            return r

def check_win(b, r, c, player):
    # Horizontal
    count = 0
    for i in range(COLS):
        if b[r][i] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for i in range(ROWS):
        if b[i][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        row = r + i
        col = c + i
        if 0 <= row < ROWS and 0 <= col < COLS:
            if b[row][col] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        row = r + i
        col = c - i
        if 0 <= row < ROWS and 0 <= col < COLS:
            if b[row][col] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(b):
    for r in range(ROWS):
        for c in range(COLS):
            if b[r][c] == " ":
                return False
    return True

def main():
    b = create_board()
    p1_turn = random.choice([True, False])
    winner = None

    print_board(b)

    while winner is None:
        if p1_turn:
            col = get_player_move(b, P1)
            row = drop_checker(b, col, P1)
            print_board(b)
            if check_win(b, row, col, P1):
                winner = P1
                print(f"{P1} won!")
                break
        else:
            col = get_player_move(b, P2)
            row = drop_checker(b, col, P2)
            print_board(b)
            if check_win(b, row, col, P2):
                winner = P2
                print(f"{P2} won!")
                break

        if check_draw(b):
            print("Draw!")
            break

        p1_turn = not p1_turn

if __name__ == "__main__":
    main()
```