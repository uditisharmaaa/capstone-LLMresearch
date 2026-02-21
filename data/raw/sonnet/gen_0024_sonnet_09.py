# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 24
# filename        : gen_0024_sonnet_09.py
# timestamp       : 2026-02-19T20:40:41Z
# model           : anthropic/claude-3.5-sonnet
# model_short     : sonnet
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 420
# tokens_output   : 911
# tokens_total    : 1331
# cost_usd        : 0.014925
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '
PIECES = ['X', 'O']

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    for row in board:
        print("+---" * COLS + "+")
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
    print("+---" * COLS + "+")

def is_valid_column(col_letter):
    return col_letter in 'ABCDEFG'

def get_column_number(col_letter):
    return ord(col_letter) - ord('A')

def is_column_full(board, col):
    return board[0][col] != EMPTY

def drop_piece(board, col, piece):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row
    return -1

def check_win(board, row, col, piece):
    # Check horizontal
    for c in range(COLS-3):
        if all(board[row][c+i] == piece for i in range(4)):
            return True
            
    # Check vertical
    for r in range(ROWS-3):
        if all(board[r+i][col] == piece for i in range(4)):
            return True
            
    # Check diagonal (positive slope)
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
                
    # Check diagonal (negative slope)
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
                
    return False

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    game_over = False
    
    while not game_over:
        print_board(board)
        piece = PIECES[current_player]
        
        while True:
            try:
                col_letter = input(f"Player {piece}, choose a column (A-G): ").upper()
                if not is_valid_column(col_letter):
                    print("Invalid column! Please choose A-G.")
                    continue
                    
                col = get_column_number(col_letter)
                if is_column_full(board, col):
                    print("Column is full! Choose another.")
                    continue
                    
                break
            except ValueError:
                print("Invalid input! Please enter a letter A-G.")
        
        row = drop_piece(board, col, piece)
        
        if check_win(board, row, col, piece):
            print_board(board)
            print(f"Player {piece} won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()