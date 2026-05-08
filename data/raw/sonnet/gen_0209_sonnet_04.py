# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 209
# filename        : gen_0209_sonnet_04.py
# timestamp       : 2026-04-06T10:16:33Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1318
# tokens_total    : 1739
# cost_usd        : 0.021033
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

import os
import random

# Global constants
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
CONNECT_N = 4  # Number of checkers in a row needed to win

def create_board():
    """Create and return an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print board with rows
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for col in range(COLS):
            row_str += f' {board[row][col]} |'
        print(row_str)
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col_idx):
    """Check if a move is valid."""
    return board[0][col_idx] == EMPTY

def drop_checker(board, col_idx, player_symbol):
    """Drop a checker into the specified column."""
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player_symbol
            return row
    return -1  # Column is full (should not happen with validation)

def check_win(board, row, col, player_symbol):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal (down-right)
        [(1, -1)]             # Diagonal (down-left)
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in the direction
        dr, dc = direction[0]
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
            count += 1
            r += dr
            c += dc
        
        # Check in the opposite direction
        dr, dc = -dr, -dc
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
            count += 1
            r += dr
            c += dc
        
        if count >= CONNECT_N:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def get_valid_move(board, player_symbol):
    """Get and validate a move from the player."""
    while True:
        try:
            move = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            # Check if input is a single letter
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter A through G.")
                continue
            
            # Convert letter to column index
            col_idx = ord(move) - ord('A')
            
            # Check if column is within range
            if col_idx < 0 or col_idx >= COLS:
                print("Please enter a letter A through G.")
                continue
            
            # Check if column is not full
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another.")
                continue
            
            return col_idx
            
        except Exception as e:
            print(f"Invalid input. Please try again. {e}")

def play_connect4():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get valid move from player
        col_idx = get_valid_move(board, player_symbol)
        
        # Drop checker and get the row where it landed
        row = drop_checker(board, col_idx, player_symbol)
        
        # Print updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        # Switch players
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_connect4()