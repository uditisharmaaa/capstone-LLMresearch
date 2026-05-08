# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 233
# filename        : gen_0233_sonnet_13.py
# timestamp       : 2026-04-06T10:21:33Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 417
# tokens_output   : 1139
# tokens_total    : 1556
# cost_usd        : 0.018336
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

# Global constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_TOKENS = ['X', 'O']
EMPTY = ' '
CONNECT_COUNT = 4

def initialize_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print rows
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col_idx):
    """Check if a move is valid (column is not full)."""
    return board[0][col_idx] == EMPTY

def drop_token(board, col_idx, token):
    """Drop a token in the specified column."""
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = token
            return row
    return -1  # Should never reach here if is_valid_move is called first

def check_win(board, row, col, token):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)],  # Diagonal /
        [(1, -1), (-1, 1)]   # Diagonal \
    ]
    
    for direction_pair in directions:
        count = 1  # Start with 1 for the piece just placed
        
        for dr, dc in direction_pair:
            r, c = row, col
            
            while True:
                r += dr
                c += dc
                
                if (0 <= r < ROWS and 0 <= c < COLS and board[r][c] == token):
                    count += 1
                else:
                    break
            
        if count >= CONNECT_COUNT:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_column_choice(board, player_name):
    """Get and validate a column choice from the player."""
    while True:
        try:
            choice = input(f"{player_name}, choose a column (A-G): ").strip().upper()
            
            if len(choice) != 1 or not 'A' <= choice <= 'G':
                print("Please enter a letter from A to G.")
                continue
            
            col_idx = ord(choice) - ord('A')
            
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another column.")
                continue
            
            return col_idx
            
        except Exception as e:
            print(f"Invalid input. Please enter a letter from A to G.")

def play_game():
    """Main game function."""
    board = initialize_board()
    
    # Randomly determine the starting player
    current_player = random.randint(0, PLAYERS-1)
    
    print_board(board)
    
    while True:
        player_name = f"Player {current_player+1} ({PLAYER_TOKENS[current_player]})"
        
        col_idx = get_column_choice(board, player_name)
        row_idx = drop_token(board, col_idx, PLAYER_TOKENS[current_player])
        
        print_board(board)
        
        # Check for win
        if check_win(board, row_idx, col_idx, PLAYER_TOKENS[current_player]):
            print(f"{player_name} won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch to the next player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()