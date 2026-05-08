# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 248
# filename        : gen_0248_sonnet_13.py
# timestamp       : 2026-04-06T10:25:18Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 417
# tokens_output   : 1318
# tokens_total    : 1735
# cost_usd        : 0.021021
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
EMPTY = ' '
PLAYER_TOKENS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS) + '')
    
    # Print board
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for col in range(COLS):
            row_str += ' ' + board[row][col] + ' |'
        print(row_str)
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col_index):
    """Check if a move is valid (column not full)."""
    return board[0][col_index] == EMPTY

def make_move(board, col_index, player_token):
    """Place a token in the specified column."""
    # Find the lowest empty row
    for row in range(ROWS-1, -1, -1):
        if board[row][col_index] == EMPTY:
            board[row][col_index] = player_token
            return row
    return -1  # This should never happen if is_valid_move is checked first

def check_win(board, row, col, player_token):
    """Check if the current move results in a win."""
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if all(board[row][c+i] == player_token for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == player_token for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                   range(max(0, col-3), min(col+1, COLS-3))):
        if (r+3 < ROWS and c+3 < COLS and 
            all(board[r+i][c+i] == player_token for i in range(4))):
            return True
    
    # Check diagonal (down-left)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                   range(min(col+3, COLS-1), max(col-1, 2), -1)):
        if (r+3 < ROWS and c-3 >= 0 and 
            all(board[r+i][c-i] == player_token for i in range(4))):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_player_move(board):
    """Get and validate a player's move."""
    while True:
        try:
            move = input("Enter column (A-G): ").upper()
            if len(move) != 1 or move not in COLUMN_LABELS:
                print("Invalid input! Please enter a letter from A to G.")
                continue
            
            col_index = COLUMN_LABELS.index(move)
            if not is_valid_move(board, col_index):
                print("Column is full! Choose another column.")
                continue
            
            return col_index
        except Exception:
            print("Invalid input! Please enter a letter from A to G.")

def play_game():
    """Main game loop."""
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    game_over = False
    
    print_board(board)
    print(f"Player {PLAYER_TOKENS[current_player]} goes first!")
    
    while not game_over:
        print(f"Player {PLAYER_TOKENS[current_player]}'s turn")
        
        col_index = get_player_move(board)
        row_index = make_move(board, col_index, PLAYER_TOKENS[current_player])
        
        print_board(board)
        
        # Check for win
        if check_win(board, row_index, col_index, PLAYER_TOKENS[current_player]):
            print(f"Player {PLAYER_TOKENS[current_player]} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch to the next player
            current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()