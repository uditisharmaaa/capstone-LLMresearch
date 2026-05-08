# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 152
# filename        : gen_0152_sonnet_07.py
# timestamp       : 2026-04-06T10:06:11Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1461
# tokens_total    : 1881
# cost_usd        : 0.023175
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

# Global constants for the game
NUM_ROWS = 6
NUM_COLS = 7
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
NUM_PLAYERS = 2
CONNECT_N = 4  # Number of pieces needed in a row to win

def initialize_board():
    """Create an empty board filled with spaces."""
    return [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Display the board with column labels."""
    # Clear the screen first
    os.system('clear')
    
    # Print column headers (A through G)
    print("   A   B   C   D   E   F   G")
    
    # Print the board with horizontal separators
    for row in range(NUM_ROWS):
        print("+---+---+---+---+---+---+---+")
        row_display = "|"
        for col in range(NUM_COLS):
            row_display += f" {board[row][col]} |"
        print(row_display)
    
    # Print the bottom border
    print("+---+---+---+---+---+---+---+")

def get_column_choice(player_symbol):
    """Get and validate the player's column choice."""
    while True:
        try:
            choice = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            # Check if input is a single letter
            if len(choice) != 1:
                print("Please enter a single letter.")
                continue
                
            # Convert letter to column index (A=0, B=1, etc.)
            col = ord(choice) - ord('A')
            
            # Check if the column is valid
            if col < 0 or col >= NUM_COLS:
                print("Invalid column. Please choose a letter from A to G.")
                continue
                
            return col
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def is_column_full(board, col):
    """Check if a column is full."""
    # If the top row of the column has a piece, the column is full
    return board[0][col] != EMPTY

def drop_piece(board, col, player_symbol):
    """Drop a piece into the selected column."""
    # Start from the bottom row and move up
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player_symbol
            return row  # Return the row where the piece landed
    
    # This should never happen if we check is_column_full first
    return -1

def check_win(board, row, col, player_symbol):
    """Check if the current move results in a win."""
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal (down-right)
        [(1, -1)]             # Diagonal (down-left)
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the current piece
        
        # Check in the direction
        delta_row, delta_col = direction[0]
        
        # Look in positive direction
        r, c = row + delta_row, col + delta_col
        while 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == player_symbol:
            count += 1
            r += delta_row
            c += delta_col
        
        # Look in negative direction
        r, c = row - delta_row, col - delta_col
        while 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == player_symbol:
            count += 1
            r -= delta_row
            c -= delta_col
        
        # If we have 4 or more in a row, the player wins
        if count >= CONNECT_N:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    for col in range(NUM_COLS):
        if not is_column_full(board, col):
            return False
    return True

def play_connect_four():
    """Main game function."""
    # Initialize the game
    board = initialize_board()
    
    # Randomly select the starting player
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Game loop
    game_over = False
    
    # Display initial board
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get player's move
        while True:
            col = get_column_choice(player_symbol)
            
            # Check if the column is full
            if is_column_full(board, col):
                print("That column is full. Please choose another.")
                continue
            
            # Valid move, break out of the input loop
            break
        
        # Drop the piece and get the row where it landed
        row = drop_piece(board, col, player_symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch to the other player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_connect_four()