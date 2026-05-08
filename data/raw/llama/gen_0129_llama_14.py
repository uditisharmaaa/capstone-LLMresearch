# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 129
# filename        : gen_0129_llama_14.py
# timestamp       : 2026-04-06T09:59:08Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 816
# tokens_total    : 1206
# cost_usd        : 0.000815
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

def print_board(b):
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for r in b:
        print('| ' + ' | '.join(r) + ' |')
        print('+---+---+---+---+---+---+---+')

def is_valid_move(b, c):
    return b[0][c] == ' '

def get_move(b, p):
    while True:
        m = input(f"Player {p}, choose a column (A-G): ").strip().upper()
        if len(m)!= 1 or not 'A' <= m <= 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        c = ord(m) - ord('A')
        if not is_valid_move(b, c):
            print("Column is full. Please choose another column.")
            continue
        return c

def drop_checker(b, c, p):
    for r in range(ROWS - 1, -1, -1):
        if b[r][c] == ' ':
            b[r][c] = 'X' if p == 0 else 'O'
            return

def check_win(b, p):
    s = 'X' if p == 0 else 'O'
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if b[r][c] == s and b[r][c + 1] == s and b[r][c + 2] == s and b[r][c + 3] == s:
                return True
    # Check vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if b[r][c] == s and b[r + 1][c] == s and b[r + 2][c] == s and b[r + 3][c] == s:
                return True
    # Check diagonal (top-left to bottom-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if b[r][c] == s and b[r + 1][c + 1] == s and b[r + 2][c + 2] == s and b[r + 3][c + 3] == s:
                return True
    # Check diagonal (bottom-left to top-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if b[r][c] == s and b[r - 1][c + 1] == s and b[r - 2][c + 2] == s and b[r - 3][c + 3] == s:
                return True
    return False

def main():
    b = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    players = ['X', 'O']
    current_player = random.randint(0, PLAYERS - 1)
    while True:
        print_board(b)
        c = get_move(b, players[current_player])
        drop_checker(b, c, current_player)
        if check_win(b, current_player):
            print_board(b)
            print(f"Player {players[current_player]} won!")
            break
        if all([b[0][c]!= ' ' for c in range(COLS)]):
            print_board(b)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()
```