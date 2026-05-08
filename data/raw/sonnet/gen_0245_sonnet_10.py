# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 245
# filename        : gen_0245_sonnet_10.py
# timestamp       : 2026-04-06T10:24:50Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1176
# tokens_total    : 1595
# cost_usd        : 0.018897
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
CONNECT = 4

def create_board():
    """Create an empty Connect 4 board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column labels
    print('   A   B   C   D   E   F   G')
    
    # Print board with rows and cells
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def get_column_choice():
    """Get and validate a column choice from the player."""
    while True:
        choice = input("Choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        col = ord(choice.upper()) - ord('A')
        if col < 0 or col >= COLS:
            print(f"Invalid column. Please choose a column between A and G.")
            continue
        
        return col

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
    
    return -1  # Column is full (this should never happen with validation)

def check_win(board, row, col, player_symbol):
    """Check if the current move resulted in a win."""
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal (down-right)
        [(1, -1)]             # Diagonal (down-left)
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the piece just placed
        
        for dr, dc in direction:
            # Check in one direction
            r, c = row + dr, col + dc
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
                r += dr
                c += dc
            
            # Check in the opposite direction
            r, c = row - dr, col - dc
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_symbol:
                count += 1
                r -= dr
                c -= dc
        
        if count >= CONNECT:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {player_symbol}'s turn")
        
        # Get valid column choice
        while True:
            col = get_column_choice()
            if is_column_full(board, col):
                print("That column is full. Choose another.")
            else:
                break
        
        # Drop checker and get the row where it landed
        row = drop_checker(board, col, player_symbol)
        
        # Print updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()