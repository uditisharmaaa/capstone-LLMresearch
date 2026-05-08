# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 249
# filename        : gen_0249_gemini_14.py
# timestamp       : 2026-04-06T10:25:25Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 375
# tokens_output   : 984
# tokens_total    : 1359
# cost_usd        : 0.000431
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

COLS = 7
ROWS = 6
PLAYERS = 2
P1 = "X"
P2 = "O"

def clear():
    os.system('clear')

def create_board():
    b = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    return b

def print_board(b):
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for r in range(ROWS):
        print("+---" * COLS + "+")
        print("| " + " | ".join(b[r]) + " |")
    print("+---" * COLS + "+")

def get_player_move(b, p):
    while True:
        move = input(f"Player {p}, enter column (A-G): ").upper()
        if not move.isalpha() or len(move) != 1 or move < 'A' or move > 'G':
            print("Invalid input. Please enter a letter A-G.")
            continue
        c = ord(move) - ord('A')
        if b[0][c] != " ":
            print("Column is full. Please choose another column.")
            continue
        return c

def drop_checker(b, c, p):
    for r in range(ROWS - 1, -1, -1):
        if b[r][c] == " ":
            b[r][c] = p
            return r

def check_win(b, r, c, p):
    # Horizontal
    count = 0
    for i in range(COLS):
        if b[r][i] == p:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for i in range(ROWS):
        if b[i][c] == p:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Diagonal (top-left to bottom-right)
    count = 0
    row = r - min(r, c)
    col = c - min(r, c)
    while row < ROWS and col < COLS:
        if b[row][col] == p:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        row += 1
        col += 1

    # Diagonal (top-right to bottom-left)
    count = 0
    row = r - min(r, COLS - 1 - c)
    col = c + min(r, COLS - 1 - c)
    while row < ROWS and col >= 0:
        if b[row][col] == p:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        row += 1
        col -= 1

    return False

def check_draw(b):
    for c in range(COLS):
        if b[0][c] == " ":
            return False
    return True

def play_game():
    b = create_board()
    p1 = random.choice([P1, P2])
    p2 = P2 if p1 == P1 else P1
    turn = 0
    current_player = p1

    while True:
        clear()
        print_board(b)
        c = get_player_move(b, current_player)
        r = drop_checker(b, c, current_player)

        if check_win(b, r, c, current_player):
            clear()
            print_board(b)
            print(f"Player {current_player} won!")
            break

        if check_draw(b):
            clear()
            print_board(b)
            print("Draw!")
            break

        current_player = p2 if current_player == p1 else p1
        turn += 1

if __name__ == "__main__":
    play_game()
```