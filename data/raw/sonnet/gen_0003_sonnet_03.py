# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 3
# filename        : gen_0003_sonnet_03.py
# timestamp       : 2026-02-19T20:29:28Z
# model           : anthropic/claude-3.5-sonnet
# model_short     : sonnet
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 1037
# tokens_total    : 1452
# cost_usd        : 0.016800
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

import os
import random

# Game constants
ROWS = 6
COLS = 7
PLAYERS = ['X', 'O']
EMPTY = ' '
WIN_LENGTH = 4

def create_board():
    # Create empty board filled with spaces
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    # Clear screen first
    os.system('clear')
    
    # Print column headers A-G
    print('   A   B   C   D   E   F   G')
    
    # Print each row with cell borders
    for row in board:
        print('+---' * COLS + '+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    print('+---' * COLS + '+')

def is_valid_move(col, board):
    # Check if column is in range A-G and not full
    if not ('A' <= col <= 'G'):
        return False
    col_idx = ord(col) - ord('A')
    return board[0][col_idx] == EMPTY

def drop_checker(col, player, board):
    # Convert letter to column index
    col_idx = ord(col) - ord('A')
    
    # Find lowest empty row in column
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player
            return row

def check_win(row, col, player, board):
    # Convert column letter to index
    col = ord(col) - ord('A')
    
    # Check horizontal
    for c in range(max(0, col-3), min(COLS-3, col+1)):
        if all(board[row][c+i] == player for i in range(4)):
            return True
            
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == player for i in range(4)):
            return True
            
    # Check diagonal up-right
    for r in range(max(0, row-3), min(ROWS-3, row+1)):
        for c in range(max(0, col-3), min(COLS-3, col+1)):
            if all(board[r+i][c+i] == player for i in range(4)):
                return True
                
    # Check diagonal up-left
    for r in range(max(0, row-3), min(ROWS-3, row+1)):
        for c in range(max(3, col), min(COLS, col+4)):
            if all(board[r+i][c-i] == player for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    # Check if any empty spaces remain
    return all(cell != EMPTY for row in board for cell in row)

def play_game():
    # Initialize game
    board = create_board()
    current_player = random.choice(PLAYERS)
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get valid move from player
        while True:
            try:
                col = input("Choose column (A-G): ").upper()
                if is_valid_move(col, board):
                    break
                print("Invalid move. Try again.")
            except:
                print("Invalid input. Try again.")
        
        # Make move and check for win
        row = drop_checker(col, current_player, board)
        if check_win(row, col, current_player, board):
            print_board(board)
            print(f"Player {current_player} won!")
            break
            
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("Game is a draw!")
            break
            
        # Switch players
        current_player = PLAYERS[1] if current_player == PLAYERS[0] else PLAYERS[0]

if __name__ == "__main__":
    play_game()