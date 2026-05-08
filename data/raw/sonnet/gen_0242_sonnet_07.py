# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 242
# filename        : gen_0242_sonnet_07.py
# timestamp       : 2026-04-06T10:24:24Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1543
# tokens_total    : 1963
# cost_usd        : 0.024405
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

# Global constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '

def initialize_board():
    """Create an empty board filled with spaces."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Display the current state of the board."""
    # Clear the screen first
    os.system('clear')
    
    # Print column labels
    print("   A   B   C   D   E   F   G")
    
    # Print the board with rows and columns
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for col in range(COLS):
            row_str += f" {board[row][col]} |"
        print(row_str)
    
    # Print the bottom border
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    """Check if a move is valid (column exists and is not full)."""
    # Check if column is within range
    if col < 0 or col >= COLS:
        return False
    
    # Check if the top position in the column is empty
    return board[0][col] == EMPTY

def make_move(board, col, player_symbol):
    """Place a player's piece in the specified column."""
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player_symbol
            return row  # Return the row where the piece was placed

def check_win(board, row, col, player_symbol):
    """Check if the most recent move resulted in a win."""
    # Check horizontal win
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if (board[row][c] == player_symbol and 
            board[row][c+1] == player_symbol and 
            board[row][c+2] == player_symbol and 
            board[row][c+3] == player_symbol):
            return True
    
    # Check vertical win
    if row <= ROWS - 4:
        if (board[row][col] == player_symbol and 
            board[row+1][col] == player_symbol and 
            board[row+2][col] == player_symbol and 
            board[row+3][col] == player_symbol):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if (board[r][c] == player_symbol and 
            board[r+1][c+1] == player_symbol and 
            board[r+2][c+2] == player_symbol and 
            board[r+3][c+3] == player_symbol):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS-1, row+3), max(row, 3)-1, -1), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if (board[r][c] == player_symbol and 
            board[r-1][c+1] == player_symbol and 
            board[r-2][c+2] == player_symbol and 
            board[r-3][c+3] == player_symbol):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def get_player_move(board, player):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {player}, choose a column (A-G): ").upper()
            
            # Check if input is a single letter
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter from A to G.")
                continue
            
            # Convert letter to column index (A=0, B=1, etc.)
            col = ord(move) - ord('A')
            
            # Check if column is valid
            if col < 0 or col >= COLS:
                print(f"Column must be between A and G.")
                continue
            
            # Check if column is not full
            if not is_valid_move(board, col):
                print("That column is full. Choose another column.")
                continue
            
            return col
            
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def main():
    """Main game loop."""
    # Initialize the game
    board = initialize_board()
    
    # Randomly select first player (0 or 1)
    current_player = random.randint(0, PLAYERS-1)
    
    # Display initial board
    print_board(board)
    
    # Game loop
    while True:
        # Get current player's symbol
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get player's move
        col = get_player_move(board, player_symbol)
        
        # Make the move
        row = make_move(board, col, player_symbol)
        
        # Display updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, player_symbol):
            print(f"Player {player_symbol} won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()