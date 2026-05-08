# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 457
# filename        : gen_0457_sonnet46_15.py
# timestamp       : 2026-05-07T22:42:15Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 418
# tokens_output   : 902
# tokens_total    : 1320
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
#   Write in a straightforward, no-frills style.
# ====================================================================

import os
import random

NUM_COLS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2

def make_board():
    board = []
    for r in range(NUM_ROWS):
        row = []
        for c in range(NUM_COLS):
            row.append(' ')
        board.append(row)
    return board

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    for r in range(NUM_ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for c in range(NUM_COLS):
            row_str += ' ' + board[r][c] + ' |'
        print(row_str)
    print('+---+---+---+---+---+---+---+')

def get_column(board):
    col_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    while True:
        user_input = input('Choose a column (A-G): ')
        if not user_input.isalpha():
            print('Invalid input. Please enter a letter.')
            continue
        user_input = user_input.upper()
        if user_input not in col_letters:
            print('Invalid column. Please enter a letter between A and G.')
            continue
        col_index = col_letters.index(user_input)
        if board[0][col_index] != ' ':
            print('That column is full. Choose another.')
            continue
        return col_index

def drop_checker(board, col, checker):
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = checker
            return r
    return -1

def check_win(board, row, col, checker):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        r = row + dr
        c = col + dc
        while 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == checker:
            count += 1
            r += dr
            c += dc
        r = row - dr
        c = col - dc
        while 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == checker:
            count += 1
            r -= dr
            c -= dc
        if count >= 4:
            return True
    return False

def check_draw(board):
    for c in range(NUM_COLS):
        if board[0][c] == ' ':
            return False
    return True

def main():
    board = make_board()
    checkers = ['X', 'O']
    current_player = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        checker = checkers[current_player]
        print('Player ' + checker + "'s turn.")
        col = get_column(board)
        row = drop_checker(board, col, checker)
        print_board(board)
        if check_win(board, row, col, checker):
            print('Player ' + checker + ' won!')
            break
        if check_draw(board):
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

main()