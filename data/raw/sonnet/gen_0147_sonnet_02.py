# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 147
# filename        : gen_0147_sonnet_02.py
# timestamp       : 2026-04-06T10:05:02Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 418
# tokens_output   : 873
# tokens_total    : 1291
# cost_usd        : 0.014349
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

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
WIN_COUNT = 4

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY

def drop_checker(board, col, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = symbol
            return row
    return -1

def check_win(board, row, col, symbol):
    directions = [
        [(0, 1), (0, -1)],  # horizontal
        [(1, 0), (-1, 0)],  # vertical
        [(1, 1), (-1, -1)],  # diagonal /
        [(1, -1), (-1, 1)]   # diagonal \
    ]
    
    for dir_pair in directions:
        count = 1
        for dr, dc in dir_pair:
            r, c = row + dr, col + dc
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == symbol:
                count += 1
                r += dr
                c += dc
        if count >= WIN_COUNT:
            return True
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_column_choice(board):
    while True:
        try:
            choice = input("Enter column (A-G): ").upper()
            if len(choice) != 1 or not 'A' <= choice <= 'G':
                print("Please enter a valid column letter A-G.")
                continue
            
            col = ord(choice) - ord('A')
            if not is_valid_move(board, col):
                print("Column is full. Choose another.")
                continue
            
            return col
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def play_connect4():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    symbol = PLAYER_SYMBOLS[current_player]
    print_board(board)
    
    while True:
        print(f"Player {symbol}'s turn")
        col = get_column_choice(board)
        row = drop_checker(board, col, symbol)
        print_board(board)
        
        if check_win(board, row, col, symbol):
            print(f"Player {symbol} won!")
            break
        
        if is_board_full(board):
            print("Game ended in a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS
        symbol = PLAYER_SYMBOLS[current_player]

if __name__ == "__main__":
    play_connect4()