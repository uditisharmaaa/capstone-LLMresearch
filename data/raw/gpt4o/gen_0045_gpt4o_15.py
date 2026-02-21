# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 45
# filename        : gen_0045_gpt4o_15.py
# timestamp       : 2026-02-19T20:45:48Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 388
# tokens_output   : 767
# tokens_total    : 1155
# cost_usd        : 0.008640
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

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_column(board, col):
    return 0 <= col < COLUMN_COUNT and board[0][col] == ' '

def get_next_open_row(board, col):
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == ' ':
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def is_board_full(board):
    for c in range(COLUMN_COUNT):
        if board[0][c] == ' ':
            return False
    return True

def play_game():
    board = create_board()
    game_over = False
    turn = random.randint(0, 1)

    while not game_over:
        print_board(board)
        col = -1
        while col == -1:
            move = input(f"Player {PLAYERS[turn]}, make your move (A-G): ").upper()
            if move in "ABCDEFG":
                col = ord(move) - ord('A')
                if not is_valid_column(board, col):
                    col = -1
            if col == -1:
                print("Invalid move. Try again.")
        
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, PLAYERS[turn])

        if winning_move(board, PLAYERS[turn]):
            print_board(board)
            print(f"Player {PLAYERS[turn]} won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            game_over = True

        turn = (turn + 1) % 2

play_game()