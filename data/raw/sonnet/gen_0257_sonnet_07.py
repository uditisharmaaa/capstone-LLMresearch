# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 257
# filename        : gen_0257_sonnet_07.py
# timestamp       : 2026-04-06T10:26:35Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1368
# tokens_total    : 1788
# cost_usd        : 0.021780
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
ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_CELL = ' '

def create_board():
    """Create a new empty board."""
    return [[EMPTY_CELL for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    # Clear the screen first
    os.system('clear')
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print board with rows
    for row in range(ROWS):
        print('+---' * COLUMNS + '+')
        print('|', end='')
        for col in range(COLUMNS):
            print(f' {board[row][col]} |', end='')
        print()
    
    # Print bottom border
    print('+---' * COLUMNS + '+')

def is_valid_move(board, column_idx):
    """Check if a move is valid (column not full)."""
    return board[0][column_idx] == EMPTY_CELL

def drop_checker(board, column_idx, player_symbol):
    """Drop a checker into the specified column."""
    # Start from the bottom row and move up
    for row in range(ROWS - 1, -1, -1):
        if board[row][column_idx] == EMPTY_CELL:
            board[row][column_idx] = player_symbol
            return row
    return -1  # Should never reach here if is_valid_move was checked

def get_player_move(board, player_symbol):
    """Get and validate the player's move."""
    while True:
        try:
            move = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            # Check if the input is a valid column letter
            if move not in COLUMN_LABELS:
                print("Invalid column! Please enter a letter A through G.")
                continue
            
            column_idx = COLUMN_LABELS.index(move)
            
            # Check if the column is not full
            if not is_valid_move(board, column_idx):
                print("That column is full! Choose another column.")
                continue
            
            return column_idx
            
        except (ValueError, IndexError):
            print("Invalid input! Please enter a letter A through G.")

def check_win(board, row, col, player_symbol):
    """Check if the last move resulted in a win."""
    # Define all possible directions: horizontal, vertical, diagonal
    directions = [
        [(0, 1)],  # Horizontal
        [(1, 0)],  # Vertical
        [(1, 1)],  # Diagonal down-right
        [(1, -1)]  # Diagonal down-left
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the just-placed piece
        
        # Check in the direction
        dr, dc = direction[0]
        r, c = row + dr, col + dc
        
        # Count consecutive pieces in the direction
        while (0 <= r < ROWS and 0 <= c < COLUMNS and 
               board[r][c] == player_symbol):
            count += 1
            r += dr
            c += dc
        
        # Check in the opposite direction
        dr, dc = -dr, -dc
        r, c = row + dr, col + dc
        
        # Count consecutive pieces in the opposite direction
        while (0 <= r < ROWS and 0 <= c < COLUMNS and 
               board[r][c] == player_symbol):
            count += 1
            r += dr
            c += dc
        
        # If 4 or more in a row, it's a win
        if count >= 4:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    for col in range(COLUMNS):
        if board[0][col] == EMPTY_CELL:
            return False
    return True

def play_connect4():
    """Main function to play the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get the player's move
        column_idx = get_player_move(board, player_symbol)
        
        # Drop the checker and get the row where it landed
        row = drop_checker(board, column_idx, player_symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check if the move resulted in a win
        if check_win(board, row, column_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        # Check if the board is full (draw)
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch to the next player
            current_player = (current_player + 1) % PLAYERS

# Start the game
if __name__ == "__main__":
    play_connect4()