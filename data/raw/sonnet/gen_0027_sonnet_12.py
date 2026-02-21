# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 27
# filename        : gen_0027_sonnet_12.py
# timestamp       : 2026-02-19T20:41:37Z
# model           : anthropic/claude-3.5-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1132
# tokens_total    : 1550
# cost_usd        : 0.018234
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = ['X', 'O']
WIN_LENGTH = 4

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

def is_valid_column(col_letter):
    return col_letter in 'ABCDEFG'

def get_column_number(col_letter):
    return ord(col_letter) - ord('A')

def is_column_full(board, col):
    return board[0][col] != ' '

def drop_checker(board, col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row
    return -1

def check_horizontal(board, row, col, player):
    count = 0
    for c in range(max(0, col-3), min(COLS, col+4)):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_vertical(board, row, col, player):
    count = 0
    for r in range(max(0, row-3), min(ROWS, row+4)):
        if board[r][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_diagonal(board, row, col, player):
    # Check diagonal up-right
    count = 0
    for i in range(-3, 4):
        r, c = row-i, col+i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    
    # Check diagonal up-left
    count = 0
    for i in range(-3, 4):
        r, c = row-i, col-i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def check_win(board, row, col, player):
    return (check_horizontal(board, row, col, player) or
            check_vertical(board, row, col, player) or
            check_diagonal(board, row, col, player))

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_move(board):
    while True:
        try:
            col_letter = input("Enter column (A-G): ").upper()
            if not is_valid_column(col_letter):
                print("Invalid column! Please enter A-G.")
                continue
            col = get_column_number(col_letter)
            if is_column_full(board, col):
                print("Column is full! Choose another.")
                continue
            return col
        except ValueError:
            print("Invalid input! Please enter a letter A-G.")

def play_game():
    board = create_board()
    current_player = random.choice(PLAYERS)
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn")
        col = get_valid_move(board)
        row = drop_checker(board, col, current_player)
        print_board(board)
        
        if check_win(board, row, col, current_player):
            print(f"Player {current_player} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()