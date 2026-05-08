# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 167
# filename        : gen_0167_sonnet_07.py
# timestamp       : 2026-04-06T10:09:28Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1583
# tokens_total    : 2003
# cost_usd        : 0.025005
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
COLUMNS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Create a new empty Connect 4 board."""
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')  # Clear the screen
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS) + '')
    
    # Print the board with rows and cells
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for col in range(COLUMNS):
            row_str += ' ' + board[row][col] + ' |'
        print(row_str)
    
    # Print the bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, column_index):
    """Check if a move is valid (column exists and isn't full)."""
    # Check if column index is valid
    if column_index < 0 or column_index >= COLUMNS:
        return False
    
    # Check if the column is full
    return board[0][column_index] == EMPTY

def get_next_open_row(board, column_index):
    """Find the next available row in the given column."""
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row
        if board[row][column_index] == EMPTY:
            return row
    return -1  # Column is full (should not happen with valid move check)

def make_move(board, column_index, player_symbol):
    """Place a player's symbol in the specified column."""
    row = get_next_open_row(board, column_index)
    board[row][column_index] = player_symbol
    return row  # Return the row where the piece was placed

def check_win(board, row, col, player_symbol):
    """Check if the current move results in a win."""
    # Check horizontal
    for c in range(max(0, col - 3), min(col + 1, COLUMNS - 3)):
        if all(board[row][c+i] == player_symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS - 4:  # Only check if there are at least 4 rows below
        if all(board[row+i][col] == player_symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row - 3), min(row + 1, ROWS - 3)), 
                   range(max(0, col - 3), min(col + 1, COLUMNS - 3))):
        if (r + 3 < ROWS and c + 3 < COLUMNS and 
            all(board[r+i][c+i] == player_symbol for i in range(4))):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS - 1, row + 3), max(row - 1, 2), -1), 
                   range(max(0, col - 3), min(col + 1, COLUMNS - 3))):
        if (r - 3 >= 0 and c + 3 < COLUMNS and 
            all(board[r-i][c+i] == player_symbol for i in range(4))):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    return all(cell != EMPTY for row in board for cell in row)

def get_player_move(board, player):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {PLAYER_SYMBOLS[player]}, choose a column (A-G): ").upper()
            
            # Validate input is a single letter
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter from A to G.")
                continue
            
            # Convert letter to column index
            if move not in COLUMN_LABELS:
                print(f"Invalid column. Please choose from {', '.join(COLUMN_LABELS)}.")
                continue
            
            column_index = COLUMN_LABELS.index(move)
            
            # Check if the column is valid and not full
            if not is_valid_move(board, column_index):
                print("That column is full. Choose another column.")
                continue
            
            return column_index
        
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def play_connect4():
    """Main function to play the Connect 4 game."""
    # Create a new board
    board = create_board()
    
    # Randomly select the starting player
    current_player = random.randint(0, PLAYERS - 1)
    
    # Game loop
    game_over = False
    print_board(board)
    
    while not game_over:
        # Get the current player's move
        column = get_player_move(board, current_player)
        
        # Make the move
        row = make_move(board, column, PLAYER_SYMBOLS[current_player])
        
        # Display the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, column, PLAYER_SYMBOLS[current_player]):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            game_over = True
            continue
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            game_over = True
            continue
        
        # Switch to the next player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_connect4()