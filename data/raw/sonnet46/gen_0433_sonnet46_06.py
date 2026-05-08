# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 433
# filename        : gen_0433_sonnet46_06.py
# timestamp       : 2026-05-07T22:33:37Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 419
# tokens_output   : 683
# tokens_total    : 1102
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

import os
import random

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

def make_board():
    return [[' '] * COLS for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(chr(65 + c) for c in range(COLS)))
    sep = '+---' * COLS + '+'
    for row in board:
        print(sep)
        print('| ' + ' | '.join(row) + ' |')
    print(sep)

def get_move(board, player):
    while True:
        raw = input(f"Player {player}, choose a column (A-G): ")
        if len(raw) != 1 or not raw.isalpha():
            print("Invalid input. Enter a single letter A-G.")
            continue
        col = ord(raw.upper()) - 65
        if col < 0 or col >= COLS:
            print("Invalid column. Choose A-G.")
            continue
        if board[0][col] != ' ':
            print("Column is full. Choose another.")
            continue
        return col

def drop(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row

def check_win(board, row, col, checker):
    def count(dr, dc):
        r, c, n = row + dr, col + dc, 0
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            n += 1; r += dr; c += dc
        return n

    for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
        if 1 + count(dr, dc) + count(-dr, -dc) >= 4:
            return True
    return False

def is_full(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def play():
    board = make_board()
    checkers = ['X', 'O']
    current = random.randrange(NUM_PLAYERS)
    print_board(board)
    while True:
        player = checkers[current]
        col = get_move(board, player)
        row = drop(board, col, player)
        print_board(board)
        if check_win(board, row, col, player):
            print(f"Player {player} won!")
            return
        if is_full(board):
            print("It's a draw!")
            return
        current = (current + 1) % NUM_PLAYERS

play()