# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 459
# filename        : gen_0459_opus_02.py
# timestamp       : 2026-05-07T22:42:38Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 418
# tokens_output   : 614
# tokens_total    : 1032
# cost_usd        : 0.052320
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

import os
import random

ROWS, COLS, NUM_PLAYERS = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']

def print_board():
    os.system('clear')
    print('   ' + '   '.join(chr(65 + i) for i in range(COLS)))
    for row in board:
        print('+---' * COLS + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * COLS + '+')

def drop(col, player):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = player
            return True
    return False

def check_win(player):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != player:
                continue
            for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                if all(0 <= r + i*dr < ROWS and 0 <= c + i*dc < COLS and board[r + i*dr][c + i*dc] == player for i in range(4)):
                    return True
    return False

def is_full():
    return all(board[0][c] != ' ' for c in range(COLS))

def get_move(player):
    while True:
        move = input(f"Player {player}, choose column (A-G): ").strip().upper()
        if len(move) != 1 or not move.isalpha() or move < 'A' or move > 'G':
            print("Invalid input. Enter a letter A-G.")
            continue
        col = ord(move) - 65
        if board[0][col] != ' ':
            print("Column full. Try again.")
            continue
        return col

current = random.randint(0, NUM_PLAYERS - 1)
print_board()
while True:
    col = get_move(players[current])
    drop(col, players[current])
    print_board()
    if check_win(players[current]):
        print(f"{players[current]} won!")
        break
    if is_full():
        print("Draw!")
        break
    current = (current + 1) % NUM_PLAYERS