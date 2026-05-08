# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 213
# filename        : gen_0213_sonnet_08.py
# timestamp       : 2026-04-06T10:17:21Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 418
# tokens_output   : 1286
# tokens_total    : 1704
# cost_usd        : 0.020544
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
#   Write with a focus on code readability over brevity.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_PIECES = ['X', 'O']
CONNECT_N = 4  # Number of pieces needed to connect for a win

def initialize_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print the board with rows
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for col in range(COLS):
            row_str += f' {board[row][col]} |'
        print(row_str)
    
    # Print the bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col):
    """Check if a move is valid."""
    # Check if the column is within bounds and not full
    return 0 <= col < COLS and board[0][col] == EMPTY

def get_next_open_row(board, col):
    """Find the next open row in the given column."""
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1  # Column is full

def make_move(board, col, piece):
    """Place a piece on the board."""
    row = get_next_open_row(board, col)
    if row != -1:
        board[row][col] = piece
        return True
    return False

def check_win(board, piece):
    """Check if the current player has won."""
    # Check horizontal locations
    for row in range(ROWS):
        for col in range(COLS - CONNECT_N + 1):
            if all(board[row][col+i] == piece for i in range(CONNECT_N)):
                return True

    # Check vertical locations
    for col in range(COLS):
        for row in range(ROWS - CONNECT_N + 1):
            if all(board[row+i][col] == piece for i in range(CONNECT_N)):
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - CONNECT_N + 1):
        for col in range(COLS - CONNECT_N + 1):
            if all(board[row+i][col+i] == piece for i in range(CONNECT_N)):
                return True

    # Check negatively sloped diagonals
    for row in range(CONNECT_N - 1, ROWS):
        for col in range(COLS - CONNECT_N + 1):
            if all(board[row-i][col+i] == piece for i in range(CONNECT_N)):
                return True

    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_player_move(board):
    """Get and validate player's move."""
    while True:
        try:
            col_letter = input("Choose a column (A-G): ").upper()
            if len(col_letter) != 1 or not 'A' <= col_letter <= 'G':
                print("Please enter a letter between A and G.")
                continue
            
            col = ord(col_letter) - ord('A')
            
            if not is_valid_move(board, col):
                print("That column is full. Please choose another.")
                continue
            
            return col
        
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def play_connect_four():
    """Main game function."""
    board = initialize_board()
    game_over = False
    
    # Randomly select the starting player
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    print_board(board)
    
    while not game_over:
        # Get player's move
        print(f"Player {PLAYER_PIECES[current_player]}'s turn")
        col = get_player_move(board)
        
        # Make the move
        make_move(board, col, PLAYER_PIECES[current_player])
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, PLAYER_PIECES[current_player]):
            print(f"Player {PLAYER_PIECES[current_player]} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch players
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_connect_four()