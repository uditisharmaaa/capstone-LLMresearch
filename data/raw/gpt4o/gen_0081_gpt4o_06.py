# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 81
# filename        : gen_0081_gpt4o_06.py
# timestamp       : 2026-02-19T21:01:25Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 664
# tokens_total    : 1054
# cost_usd        : 0.007615
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

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, PLAYER1, PLAYER2 = ' ', 'X', 'O'
COL_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COL_LABELS))
    print('+---' * COLS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLS + '+')

def is_valid_column(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for c in range(COLS - 3):
        for r in range(ROWS):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

def get_player_move():
    while True:
        col_input = input('Choose a column (A-G): ').strip().upper()
        if len(col_input) == 1 and col_input in COL_LABELS:
            return COL_LABELS.index(col_input)
        print('Invalid input. Please try again.')

def main():
    board = create_board()
    game_over = False
    turn = random.randint(0, PLAYERS - 1)
    print_board(board)

    while not game_over:
        col = get_player_move()
        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            piece = PLAYER1 if turn == 0 else PLAYER2
            drop_piece(board, row, col, piece)
            print_board(board)

            if winning_move(board, piece):
                print(f"{piece} won!")
                game_over = True
            elif is_draw(board):
                print("It's a draw!")
                game_over = True

            turn = (turn + 1) % PLAYERS

main()