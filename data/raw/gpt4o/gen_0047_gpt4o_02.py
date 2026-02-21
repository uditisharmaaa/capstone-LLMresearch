# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 47
# filename        : gen_0047_gpt4o_02.py
# timestamp       : 2026-02-19T20:46:12Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 631
# tokens_total    : 1020
# cost_usd        : 0.007283
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

import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
BOARD = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
CHARS = ['X', 'O']
COL_LABELS = 'ABCDEFG'

def print_board():
    os.system('clear')
    print('   ' + '   '.join(COL_LABELS))
    print('+---' * COLS + '+')
    for row in BOARD:
        print('|' + '|'.join(f' {c} ' for c in row) + '|')
        print('+---' * COLS + '+')

def valid_move(col):
    return col in COL_LABELS and BOARD[0][COL_LABELS.index(col)] == ' '

def make_move(col, char):
    for row in reversed(BOARD):
        if row[COL_LABELS.index(col)] == ' ':
            row[COL_LABELS.index(col)] = char
            break

def check_winner(char):
    def check_line(a, b, c, d): return a == b == c == d == char
    for row in range(ROWS):
        for col in range(COLS - 3):
            if check_line(BOARD[row][col], BOARD[row][col+1], BOARD[row][col+2], BOARD[row][col+3]): return True
    for col in range(COLS):
        for row in range(ROWS - 3):
            if check_line(BOARD[row][col], BOARD[row+1][col], BOARD[row+2][col], BOARD[row+3][col]): return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if check_line(BOARD[row][col], BOARD[row+1][col+1], BOARD[row+2][col+2], BOARD[row+3][col+3]): return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if check_line(BOARD[row][col], BOARD[row-1][col+1], BOARD[row-2][col+2], BOARD[row-3][col+3]): return True
    return False

def board_full():
    return all(BOARD[0][col] != ' ' for col in range(COLS))

def main():
    current_player = random.randint(0, PLAYERS - 1)
    while True:
        print_board()
        move = input(f"Player {CHARS[current_player]}, choose a column (A-G): ").strip()
        if valid_move(move):
            make_move(move, CHARS[current_player])
            if check_winner(CHARS[current_player]):
                print_board()
                print(f"Player {CHARS[current_player]} won!")
                break
            if board_full():
                print_board()
                print("It's a draw!")
                break
            current_player = (current_player + 1) % PLAYERS
        else:
            print("Invalid input. Try again.")

main()