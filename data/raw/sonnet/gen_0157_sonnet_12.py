# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 157
# filename        : gen_0157_sonnet_12.py
# timestamp       : 2026-04-06T10:07:17Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1194
# tokens_total    : 1612
# cost_usd        : 0.019164
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
CONNECT_N = 4  # Number of pieces in a row needed to win

def create_board():
    """Create a new empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers
    print("   A   B   C   D   E   F   G")
    
    # Print rows
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
    
    print("+---+---+---+---+---+---+---+")

def get_column_choice(player_symbol):
    """Get and validate the player's column choice."""
    valid_columns = "ABCDEFG"
    while True:
        choice = input(f"Player {player_symbol}, choose a column (A-G): ")
        if len(choice) != 1 or choice not in valid_columns:
            print("Invalid input. Please enter a letter A through G.")
            continue
        
        col_index = ord(choice) - ord('A')
        return col_index

def is_column_full(board, col):
    """Check if a column is full."""
    return board[0][col] != EMPTY

def drop_checker(board, col, player_symbol):
    """Drop a checker in the specified column."""
    # Start from the bottom row and move up
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player_symbol
            return row
    return -1  # Column is full (should not reach here due to validation)

def check_win(board, row, col, player_symbol):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal down-right
        [(1, -1)]             # Diagonal down-left
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in the positive direction
        dr, dc = direction[0]
        for i in range(1, CONNECT_N):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
            else:
                break
                
        # Check in the negative direction
        dr, dc = -dr, -dc
        for i in range(1, CONNECT_N):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
            else:
                break
                
        if count >= CONNECT_N:
            return True
            
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    for col in range(COLS):
        if not is_column_full(board, col):
            return False
    return True

def play_game():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    
    print_board(board)
    
    while True:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get valid column choice
        while True:
            col = get_column_choice(player_symbol)
            if is_column_full(board, col):
                print("That column is full. Choose another.")
            else:
                break
        
        # Drop the checker and get the row where it landed
        row = drop_checker(board, col, player_symbol)
        
        # Print updated board
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
    play_game()