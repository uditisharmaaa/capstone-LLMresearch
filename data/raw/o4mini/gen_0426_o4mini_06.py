# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 426
# filename        : gen_0426_o4mini_06.py
# timestamp       : 2026-05-07T19:18:49Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 502
# tokens_total    : 892
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

import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']
columns = "ABCDEFG"

def clear_screen(): os.system('clear')

def print_board():
    clear_screen()
    print("   " + "   ".join(columns))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def valid_input(col):
    return col in columns and board[0][columns.index(col)] == " "

def drop_checker(player, col):
    for row in reversed(board):
        if row[columns.index(col)] == " ":
            row[columns.index(col)] = player
            break

def check_winner(player):
    for r in range(ROWS):
        for c in range(COLS):
            if c + 3 < COLS and all(board[r][c + i] == player for i in range(4)): return True
            if r + 3 < ROWS and all(board[r + i][c] == player for i in range(4)): return True
            if c + 3 < COLS and r + 3 < ROWS and all(board[r + i][c + i] == player for i in range(4)): return True
            if c - 3 >= 0 and r + 3 < ROWS and all(board[r + i][c - i] == player for i in range(4)): return True
    return False

def board_full(): return all(board[0][c] != " " for c in range(COLS))

current_player = random.choice(players)
while True:
    print_board()
    col = input(f"Player {current_player}, choose a column (A-G): ").strip().upper()
    if valid_input(col):
        drop_checker(current_player, col)
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} won!")
            break
        if board_full():
            print_board()
            print("It's a draw!")
            break
        current_player = players[(players.index(current_player) + 1) % PLAYERS]
    else:
        print("Invalid input. Try again.")