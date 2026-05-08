# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 107
# filename        : gen_0107_sonnet_07.py
# timestamp       : 2026-04-06T09:54:17Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1501
# tokens_total    : 1921
# cost_usd        : 0.023775
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

# Constants for the game
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY_SPACE = ' '
CONNECT_COUNT = 4

def create_board():
    """Create an empty board filled with spaces"""
    return [[EMPTY_SPACE for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board"""
    # Clear the screen first
    os.system('clear')
    
    # Print column headers (A through G)
    print("   A   B   C   D   E   F   G")
    
    # Print the board with rows and separators
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(COLS):
            print(f" {board[row][col]} |", end="")
        print()  # New line after each row
    
    # Print the bottom border
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col_idx):
    """Check if a move is valid (column has space)"""
    # Check if the top row of the selected column is empty
    return board[0][col_idx] == EMPTY_SPACE

def drop_checker(board, col_idx, player_symbol):
    """Drop a checker into the specified column"""
    # Start from the bottom row and move up until finding an empty space
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY_SPACE:
            board[row][col_idx] = player_symbol
            return row  # Return the row where the checker was placed
    
    # This should never happen if is_valid_move is called before this function
    return -1

def get_valid_column_choice(board):
    """Get a valid column choice from the player"""
    while True:
        try:
            col_choice = input("Choose a column (A-G): ").upper()
            
            # Check if input is a single letter
            if len(col_choice) != 1 or not col_choice.isalpha():
                print("Please enter a single letter A through G.")
                continue
            
            # Convert letter to column index (A=0, B=1, etc.)
            col_idx = ord(col_choice) - ord('A')
            
            # Check if column is within range
            if col_idx < 0 or col_idx >= COLS:
                print(f"Please choose a column between A and G.")
                continue
            
            # Check if the column has space
            if not is_valid_move(board, col_idx):
                print(f"Column {col_choice} is full. Choose another column.")
                continue
            
            return col_idx
            
        except Exception as e:
            print("Invalid input. Please try again.")

def check_win(board, row, col, player_symbol):
    """Check if the current move resulted in a win"""
    # Define the directions to check: horizontal, vertical, diagonal up, diagonal down
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)], # Diagonal up-right to down-left
        [(1, -1), (-1, 1)]  # Diagonal up-left to down-right
    ]
    
    for direction_pair in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in both directions
        for dr, dc in direction_pair:
            r, c = row, col
            
            # Move in the current direction and count matching pieces
            while True:
                r += dr
                c += dc
                
                # Check if we're still on the board
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    break
                
                # Check if the piece matches
                if board[r][c] != player_symbol:
                    break
                
                count += 1
                
                # If we found 4 in a row, return True
                if count >= CONNECT_COUNT:
                    return True
    
    # No win found
    return False

def is_board_full(board):
    """Check if the board is completely full"""
    for col in range(COLS):
        if board[0][col] == EMPTY_SPACE:
            return False
    return True

def play_connect_four():
    """Main function to play Connect Four"""
    # Create an empty board
    board = create_board()
    
    # Randomly choose which player goes first
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Print the initial empty board
    print_board(board)
    
    # Game loop
    while True:
        # Get player symbol
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Display whose turn it is
        print(f"Player {player_symbol}'s turn")
        
        # Get a valid column choice
        col_idx = get_valid_column_choice(board)
        
        # Drop the checker and get the row where it landed
        row = drop_checker(board, col_idx, player_symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check for a win
        if check_win(board, row, col_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_connect_four()