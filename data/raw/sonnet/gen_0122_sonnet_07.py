# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 122
# filename        : gen_0122_sonnet_07.py
# timestamp       : 2026-04-06T09:57:24Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1445
# tokens_total    : 1865
# cost_usd        : 0.022935
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
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_TOKENS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Create an empty Connect 4 board."""
    # Initialize with empty spaces
    return [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')  # Clear the screen
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print the board with rows and dividers
    for row in range(NUM_ROWS):
        print('+---' * NUM_COLS + '+')
        row_display = '|'
        for col in range(NUM_COLS):
            row_display += f' {board[row][col]} |'
        print(row_display)
    
    # Print the bottom line
    print('+---' * NUM_COLS + '+')

def is_valid_move(board, col_idx):
    """Check if a move is valid (column not full)."""
    # Check if the top position in the selected column is empty
    return board[0][col_idx] == EMPTY

def make_move(board, col_idx, player_token):
    """Place a player's token in the specified column."""
    # Start from the bottom row and find the first empty space
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player_token
            return row  # Return the row where the token was placed
    
    # This should never happen if is_valid_move is called first
    return -1

def check_win(board, row, col, player_token):
    """Check if the current move results in a win."""
    # Check horizontal win
    for c in range(max(0, col - 3), min(col + 1, NUM_COLS - 3)):
        if all(board[row][c + i] == player_token for i in range(4)):
            return True
    
    # Check vertical win
    if row <= NUM_ROWS - 4:
        if all(board[row + i][col] == player_token for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row - 3), min(row + 1, NUM_ROWS - 3)),
                    range(max(0, col - 3), min(col + 1, NUM_COLS - 3))):
        if all(board[r + i][c + i] == player_token for i in range(4)):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(row + 3, NUM_ROWS - 1), max(row - 1, -1), -1),
                    range(max(0, col - 3), min(col + 1, NUM_COLS - 3))):
        if all(board[r - i][c + i] == player_token for i in range(4)):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    return all(board[0][col] != EMPTY for col in range(NUM_COLS))

def get_player_move(board, player):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {player}'s turn. Choose a column (A-G): ").upper()
            
            # Validate input is a letter from A to G
            if move not in COLUMN_LABELS:
                print("Invalid column. Please enter a letter from A to G.")
                continue
            
            col_idx = COLUMN_LABELS.index(move)
            
            # Check if the column is full
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another column.")
                continue
                
            return col_idx
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter a letter from A to G.")

def play_connect_four():
    """Main game function."""
    # Create an empty board
    board = create_board()
    
    # Randomly select the starting player
    current_player = random.randint(0, NUM_PLAYERS - 1)
    player_token = PLAYER_TOKENS[current_player]
    
    # Game loop
    game_over = False
    
    # Print the initial empty board
    print_board(board)
    
    while not game_over:
        # Get the player's move
        col_idx = get_player_move(board, player_token)
        
        # Make the move
        row = make_move(board, col_idx, player_token)
        
        # Print the updated board
        print_board(board)
        
        # Check for a win
        if check_win(board, row, col_idx, player_token):
            print(f"Player {player_token} won!")
            game_over = True
        # Check for a draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = (current_player + 1) % NUM_PLAYERS
            player_token = PLAYER_TOKENS[current_player]

if __name__ == "__main__":
    play_connect_four()