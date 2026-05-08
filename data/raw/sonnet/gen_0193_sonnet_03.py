# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 193
# filename        : gen_0193_sonnet_03.py
# timestamp       : 2026-04-06T10:14:05Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 1449
# tokens_total    : 1864
# cost_usd        : 0.022980
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

# Constants for game configuration
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY_CELL = ' '
CONNECT_N = 4  # Number of checkers in a row needed to win

def initialize_board():
    """Create an empty game board filled with spaces."""
    return [[EMPTY_CELL for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the game board with column labels."""
    # Clear the screen first
    os.system('clear')
    
    # Print column headers (A through G)
    print("   A   B   C   D   E   F   G")
    
    # Print each row of the board
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for col in range(COLS):
            row_str += f" {board[row][col]} |"
        print(row_str)
    
    # Print the bottom border of the board
    print("+---+---+---+---+---+---+---+")

def get_column_choice(player_symbol):
    """Get a valid column choice from the player."""
    while True:
        try:
            # Ask for input and convert to uppercase
            choice = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            # Validate the input is a single letter between A and G
            if len(choice) != 1 or not 'A' <= choice <= 'G':
                print("Please enter a letter between A and G.")
                continue
            
            # Convert letter to column index (0-6)
            col_idx = ord(choice) - ord('A')
            return col_idx
        except Exception:
            print("Invalid input. Please enter a letter between A and G.")

def is_valid_move(board, col):
    """Check if a move is valid (column is not full)."""
    # Check if the top cell in the column is empty
    return board[0][col] == EMPTY_CELL

def make_move(board, col, player_symbol):
    """Place a player's checker in the lowest available position in the chosen column."""
    # Start from the bottom row and move up to find the first empty cell
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY_CELL:
            board[row][col] = player_symbol
            return row  # Return the row where the checker was placed

def check_win(board, row, col, player_symbol):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1)],              # Horizontal
        [(1, 0)],              # Vertical
        [(1, 1)],              # Diagonal (down-right)
        [(1, -1)]              # Diagonal (down-left)
    ]
    
    # Check each direction for a win
    for direction in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in the direction
        delta_row, delta_col = direction[0]
        for i in range(1, CONNECT_N):
            r, c = row + delta_row * i, col + delta_col * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
            else:
                break
        
        # Check in the opposite direction
        delta_row, delta_col = -delta_row, -delta_col
        for i in range(1, CONNECT_N):
            r, c = row + delta_row * i, col + delta_col * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
            else:
                break
        
        # If we found 4 in a row, the player wins
        if count >= CONNECT_N:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    for col in range(COLS):
        if board[0][col] == EMPTY_CELL:
            return False
    return True

def play_game():
    """Main game function."""
    # Initialize the game board
    board = initialize_board()
    
    # Randomly select which player goes first
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Initial board display
    print_board(board)
    
    # Game loop
    while True:
        # Get the current player's symbol
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get player's column choice
        col = get_column_choice(player_symbol)
        
        # Check if the chosen column is valid
        if not is_valid_move(board, col):
            print("That column is full. Please choose another column.")
            continue
        
        # Make the move and get the row where the checker was placed
        row = make_move(board, col, player_symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, player_symbol):
            print(f"Player {player_symbol} won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

# Start the game
if __name__ == "__main__":
    play_game()