# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 236
# filename        : gen_0236_sonnet_01.py
# timestamp       : 2026-04-06T10:23:30Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1307
# tokens_total    : 1728
# cost_usd        : 0.020868
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_PIECES = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CONNECT_N = 4  # Number of pieces in a row needed to win

def create_board():
    """Create an empty game board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print top border
    print('+---' * COLS + '+')
    
    # Print rows
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * COLS + '+')

def is_valid_move(board, col):
    """Check if a move is valid."""
    # Check if the column is within range
    if col < 0 or col >= COLS:
        return False
    
    # Check if the column is full
    return board[0][col] == EMPTY

def drop_piece(board, col, piece):
    """Drop a piece into the specified column."""
    # Find the lowest empty row
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row
    return -1  # Column is full

def check_win(board, row, col, piece):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)], # Diagonal /
        [(1, -1), (-1, 1)]  # Diagonal \
    ]
    
    for dir_pair in directions:
        count = 1  # Start with the piece just placed
        
        # Check in both directions
        for dx, dy in dir_pair:
            r, c = row, col
            
            # Keep moving in this direction as long as we find matching pieces
            while True:
                r += dx
                c += dy
                
                # Check if we're still on the board
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    break
                
                # Check if the piece matches
                if board[r][c] != piece:
                    break
                
                count += 1
                
                # If we've found enough in a row, the player wins
                if count >= CONNECT_N:
                    return True
                    
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def get_column_choice(board, player_piece):
    """Get a valid column choice from the player."""
    while True:
        try:
            choice = input(f"Player {player_piece}, choose a column (A-G): ").upper()
            if len(choice) != 1 or choice not in COLUMN_LABELS:
                print("Invalid input! Please enter a letter from A to G.")
                continue
                
            col = COLUMN_LABELS.index(choice)
            
            if not is_valid_move(board, col):
                print("That column is full! Choose another one.")
                continue
                
            return col
            
        except Exception:
            print("Invalid input! Please enter a letter from A to G.")

def main():
    """Main game function."""
    # Create a new board
    board = create_board()
    
    # Randomly select which player goes first
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Game loop
    game_over = False
    
    while not game_over:
        # Clear the screen and print the board
        os.system('clear')
        print_board(board)
        
        # Get player's move
        col = get_column_choice(board, PLAYER_PIECES[current_player])
        
        # Drop the piece and get the row where it landed
        row = drop_piece(board, col, PLAYER_PIECES[current_player])
        
        # Check if the move resulted in a win
        if check_win(board, row, col, PLAYER_PIECES[current_player]):
            os.system('clear')
            print_board(board)
            print(f"Player {PLAYER_PIECES[current_player]} won!")
            game_over = True
        
        # Check if the board is full (draw)
        elif is_board_full(board):
            os.system('clear')
            print_board(board)
            print("It's a draw!")
            game_over = True
        
        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()