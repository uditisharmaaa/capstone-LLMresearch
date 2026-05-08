# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 463
# filename        : gen_0463_opus_06.py
# timestamp       : 2026-05-07T22:43:28Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 419
# tokens_output   : 787
# tokens_total    : 1206
# cost_usd        : 0.065310
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

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(chr(65 + i) for i in range(COLS)))
    for row in board:
        print('+---' * COLS + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * COLS + '+')

def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row
    return -1

def check_win(board, checker):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == checker for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == checker for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == checker for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == checker for i in range(4)):
                return True
    return False

def is_full(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def get_move(board):
    while True:
        move = input("Enter column (A-G): ").strip()
        if len(move) != 1 or not move.isalpha():
            print("Invalid input. Enter a letter A-G.")
            continue
        move = move.upper()
        if move < 'A' or move > 'G':
            print("Invalid input. Enter a letter A-G.")
            continue
        col = ord(move) - 65
        if board[0][col] != ' ':
            print("Column is full. Choose another.")
            continue
        return col

def main():
    board = create_board()
    players = ['X', 'O']
    current = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        print(f"Player {players[current]}'s turn")
        col = get_move(board)
        drop_checker(board, col, players[current])
        print_board(board)
        if check_win(board, players[current]):
            print(f"{players[current]} won!")
            break
        if is_full(board):
            print("Draw!")
            break
        current = (current + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()