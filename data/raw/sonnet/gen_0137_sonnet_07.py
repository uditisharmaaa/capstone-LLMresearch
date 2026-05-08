# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 137
# filename        : gen_0137_sonnet_07.py
# timestamp       : 2026-04-06T10:02:44Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1421
# tokens_total    : 1841
# cost_usd        : 0.022575
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

import os
import random

# Constants
NUM_ROWS = 6
NUM_COLS = 7
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'

def initialize_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear')

def print_board(board):
    """Print the current state of the board."""
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print the board with separators
    for row in range(NUM_ROWS):
        print('+---' * NUM_COLS + '+')
        print('|', end='')
        for col in range(NUM_COLS):
            print(f' {board[row][col]} |', end='')
        print()
    
    # Print the bottom border
    print('+---' * NUM_COLS + '+')

def is_valid_move(board, col_idx):
    """Check if a move is valid (column not full)."""
    return board[0][col_idx] == EMPTY

def make_move(board, col_idx, player_symbol):
    """Drop a checker into the specified column."""
    # Find the lowest empty row in the column
    for row in range(NUM_ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player_symbol
            return row
    return -1  # This should never happen with valid moves

def check_win(board, row, col, player_symbol):
    """Check if the last move resulted in a win."""
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, NUM_COLS-3)):
        if all(board[row][c+i] == player_symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= NUM_ROWS-4:
        if all(board[row+i][col] == player_symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, NUM_ROWS-3)), 
                   range(max(0, col-3), min(col+1, NUM_COLS-3))):
        if r + 3 < NUM_ROWS and c + 3 < NUM_COLS:
            if all(board[r+i][c+i] == player_symbol for i in range(4)):
                return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(NUM_ROWS-1, row+3), max(row-1, 2), -1), 
                   range(max(0, col-3), min(col+1, NUM_COLS-3))):
        if r - 3 >= 0 and c + 3 < NUM_COLS:
            if all(board[r-i][c+i] == player_symbol for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(board[0][col] != EMPTY for col in range(NUM_COLS))

def get_player_move(board, player_symbol):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            # Check if input is a single letter
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter from A to G.")
                continue
            
            # Convert letter to column index
            if move not in COLUMN_LABELS:
                print(f"Invalid column. Please choose from {', '.join(COLUMN_LABELS)}.")
                continue
            
            col_idx = COLUMN_LABELS.index(move)
            
            # Check if the column is full
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another column.")
                continue
            
            return col_idx
            
        except ValueError:
            print("Invalid input. Please try again.")

def play_connect4():
    """Main game function."""
    board = initialize_board()
    current_player = random.randint(0, 1)  # Randomly choose starting player
    game_over = False
    
    clear_screen()
    print("Welcome to Connect 4!")
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get player's move
        col_idx = get_player_move(board, player_symbol)
        
        # Make the move
        row_idx = make_move(board, col_idx, player_symbol)
        
        # Clear screen and redraw board
        clear_screen()
        print_board(board)
        
        # Check for win
        if check_win(board, row_idx, col_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_connect4()