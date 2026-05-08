# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 205
# filename        : gen_0205_sonnet_15.py
# timestamp       : 2026-04-06T10:15:41Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 418
# tokens_output   : 1075
# tokens_total    : 1493
# cost_usd        : 0.017379
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

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
CONNECT_NUM = 4

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def is_valid_move(board, col_idx):
    return board[0][col_idx] == EMPTY

def drop_checker(board, col_idx, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = symbol
            return row

def check_win(board, row, col, symbol):
    # Check horizontal
    for c in range(COLS - CONNECT_NUM + 1):
        if all(board[row][c+i] == symbol for i in range(CONNECT_NUM)):
            return True
    
    # Check vertical
    for r in range(ROWS - CONNECT_NUM + 1):
        if all(board[r+i][col] == symbol for i in range(CONNECT_NUM)):
            return True
    
    # Check diagonal (down-right)
    for r in range(ROWS - CONNECT_NUM + 1):
        for c in range(COLS - CONNECT_NUM + 1):
            if all(board[r+i][c+i] == symbol for i in range(CONNECT_NUM)):
                return True
    
    # Check diagonal (up-right)
    for r in range(CONNECT_NUM - 1, ROWS):
        for c in range(COLS - CONNECT_NUM + 1):
            if all(board[r-i][c+i] == symbol for i in range(CONNECT_NUM)):
                return True
    
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_column_choice(board, player):
    while True:
        try:
            col_letter = input(f"Player {player+1} ({PLAYER_SYMBOLS[player]}), choose a column (A-G): ")
            if not col_letter.isalpha() or len(col_letter) != 1:
                print("Please enter a single letter from A to G.")
                continue
                
            col_letter = col_letter.upper()
            col_idx = ord(col_letter) - ord('A')
            
            if col_idx < 0 or col_idx >= COLS:
                print("Please enter a letter from A to G.")
                continue
                
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another one.")
                continue
                
            return col_idx
            
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def play_game():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        col_idx = get_column_choice(board, current_player)
        row_idx = drop_checker(board, col_idx, PLAYER_SYMBOLS[current_player])
        
        print_board(board)
        
        if check_win(board, row_idx, col_idx, PLAYER_SYMBOLS[current_player]):
            print(f"Player {current_player+1} ({PLAYER_SYMBOLS[current_player]}) won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()