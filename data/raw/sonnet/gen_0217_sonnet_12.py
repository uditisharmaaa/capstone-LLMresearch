# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 217
# filename        : gen_0217_sonnet_12.py
# timestamp       : 2026-04-06T10:18:31Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1154
# tokens_total    : 1572
# cost_usd        : 0.018564
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
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
CONNECT_N = 4  # Number of pieces in a row needed to win

def create_board():
    """Create an empty game board."""
    return [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Print the game board with column labels."""
    os.system('clear')
    
    # Print column headers
    print("   A   B   C   D   E   F   G")
    
    # Print board rows
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_column_choice():
    """Get and validate the player's column choice."""
    while True:
        choice = input("Choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a letter A-G.")
            continue
        
        col_index = ord(choice.upper()) - ord('A')
        if col_index < 0 or col_index >= NUM_COLS:
            print("Invalid column. Please enter a letter A-G.")
            continue
            
        return col_index

def is_column_full(board, col):
    """Check if a column is full."""
    return board[0][col] != EMPTY

def drop_checker(board, col, symbol):
    """Drop a checker into the specified column."""
    # Find the lowest empty row in the column
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = symbol
            return row
    return -1  # Column is full (should never happen with validation)

def check_win(board, row, col, symbol):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)],  # Diagonal /
        [(1, -1), (-1, 1)]   # Diagonal \
    ]
    
    for direction_pair in directions:
        count = 1  # Count the piece that was just placed
        
        for direction in direction_pair:
            dr, dc = direction
            r, c = row + dr, col + dc
            
            while (0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and 
                   board[r][c] == symbol):
                count += 1
                r += dr
                c += dc
                
        if count >= CONNECT_N:
            return True
            
    return False

def is_board_full(board):
    """Check if the board is full (draw condition)."""
    for col in range(NUM_COLS):
        if not is_column_full(board, col):
            return False
    return True

def play_game():
    """Main game loop."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {symbol}'s turn")
        
        # Get valid column choice
        while True:
            col = get_column_choice()
            if is_column_full(board, col):
                print("That column is full. Choose another.")
            else:
                break
        
        # Drop checker and get the row where it landed
        row = drop_checker(board, col, symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, symbol):
            print(f"Player {symbol} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()