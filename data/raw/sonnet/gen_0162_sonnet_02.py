# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 162
# filename        : gen_0162_sonnet_02.py
# timestamp       : 2026-04-06T10:08:23Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 418
# tokens_output   : 1044
# tokens_total    : 1462
# cost_usd        : 0.016914
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

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for col in range(COLS):
            print(f' {board[row][col]} |', end='')
        print()
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col):
    return 0 <= col < COLS and board[0][col] == ' '

def drop_checker(board, col, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = symbol
            return row
    return -1

def check_win(board, row, col, symbol):
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if all(board[row][c+i] == symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if r + 3 < ROWS and c + 3 < COLS:
            if all(board[r+i][c+i] == symbol for i in range(4)):
                return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS-1, row+3), max(row, 3) - 1, -1), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if r - 3 >= 0 and c + 3 < COLS:
            if all(board[r-i][c+i] == symbol for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def get_column_choice(board):
    while True:
        try:
            choice = input("Choose a column (A-G): ")
            if len(choice) != 1 or not choice.isalpha():
                print("Please enter a single letter.")
                continue
            
            col = ord(choice.upper()) - ord('A')
            if not 0 <= col < COLS:
                print("Please choose a column between A and G.")
                continue
            
            if not is_valid_move(board, col):
                print("That column is full. Choose another.")
                continue
            
            return col
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    print_board(board)
    
    while True:
        symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {symbol}'s turn")
        
        col = get_column_choice(board)
        row = drop_checker(board, col, symbol)
        print_board(board)
        
        if check_win(board, row, col, symbol):
            print(f"Player {symbol} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()