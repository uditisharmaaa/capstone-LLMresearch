# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 478
# filename        : gen_0478_opus46_06.py
# timestamp       : 2026-05-07T22:47:42Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 419
# tokens_output   : 646
# tokens_total    : 1065
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

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']

def print_board():
    os.system('clear')
    print('   ' + '   '.join(chr(65 + c) for c in range(COLS)))
    for row in range(ROWS):
        print('+---' * COLS + '+')
        print('| ' + ' | '.join(board[row]) + ' |')
    print('+---' * COLS + '+')

def drop(col, checker):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = checker
            return r
    return -1

def check_win(r, c, ch):
    dirs = [(0,1),(1,0),(1,1),(1,-1)]
    for dr, dc in dirs:
        count = 1
        for s in (1, -1):
            nr, nc = r + s*dr, c + s*dc
            while 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == ch:
                count += 1
                nr += s*dr
                nc += s*dc
        if count >= 4:
            return True
    return False

def is_full():
    return all(board[0][c] != ' ' for c in range(COLS))

turn = random.randrange(NUM_PLAYERS)
print_board()
while True:
    while True:
        inp = input(f"Player {players[turn]}, choose a column (A-G): ").strip()
        if len(inp) != 1 or not inp.isalpha():
            print("Invalid input. Enter a letter A-G.")
            continue
        inp = inp.upper()
        if inp < 'A' or inp > 'G':
            print("Invalid input. Enter a letter A-G.")
            continue
        col = ord(inp) - 65
        if board[0][col] != ' ':
            print("Column is full. Choose another.")
            continue
        break
    r = drop(col, players[turn])
    print_board()
    if check_win(r, col, players[turn]):
        print(f"Player {players[turn]} won!")
        break
    if is_full():
        print("It's a draw!")
        break
    turn = (turn + 1) % NUM_PLAYERS
```