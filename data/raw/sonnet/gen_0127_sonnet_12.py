# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 127
# filename        : gen_0127_sonnet_12.py
# timestamp       : 2026-04-06T09:58:31Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1171
# tokens_total    : 1589
# cost_usd        : 0.018819
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

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS) + '   ')
    
    # Print board
    for row in range(ROWS):
        print('+---+' * COLS + '+')
        print('|', end='')
        for col in range(COLS):
            print(f' {board[row][col]} |', end='')
        print()
    print('+---+' * COLS + '+')

def is_valid_move(board, col_idx):
    # Check if the column is full
    return board[0][col_idx] == EMPTY

def get_next_open_row(board, col_idx):
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            return row
    return -1

def drop_piece(board, row, col, symbol):
    board[row][col] = symbol

def get_player_move(board, player_symbol):
    while True:
        try:
            move = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            if len(move) != 1 or move not in COLUMN_LABELS:
                print("Invalid input. Please enter a letter from A to G.")
                continue
            
            col_idx = COLUMN_LABELS.index(move)
            
            if not is_valid_move(board, col_idx):
                print("Column is full. Choose another column.")
                continue
                
            return col_idx
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def check_win(board, row, col, symbol):
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if all(board[row][c+i] == symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == symbol for i in range(4)):
            return True
    
    # Check diagonal (positive slope)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                   range(max(0, col-3), min(col+1, COLS-3))):
        if all(board[r+i][c+i] == symbol for i in range(4)):
            return True
    
    # Check diagonal (negative slope)
    for r, c in zip(range(min(row+3, ROWS-1), max(row-1, 2), -1), 
                   range(max(0, col-3), min(col+1, COLS-3))):
        if all(board[r-i][c+i] == symbol for i in range(4)):
            return True
    
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def play_game():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        # Get player move
        col_idx = get_player_move(board, PLAYER_SYMBOLS[current_player])
        
        # Drop piece
        row = get_next_open_row(board, col_idx)
        drop_piece(board, row, col_idx, PLAYER_SYMBOLS[current_player])
        
        # Print board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col_idx, PLAYER_SYMBOLS[current_player]):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch player
        current_player = (current_player + 1) % PLAYERS

def main():
    play_game()

if __name__ == "__main__":
    main()