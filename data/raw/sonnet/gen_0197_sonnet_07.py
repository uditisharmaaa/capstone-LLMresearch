# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 197
# filename        : gen_0197_sonnet_07.py
# timestamp       : 2026-04-06T10:14:31Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 1369
# tokens_total    : 1789
# cost_usd        : 0.021795
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
EMPTY_SPACE = ' '
CONNECT_COUNT = 4

def create_board():
    """Create an empty board with spaces."""
    return [[EMPTY_SPACE for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    # Clear the screen before printing
    os.system('clear')
    
    # Print column labels
    print("   A   B   C   D   E   F   G")
    
    # Print board rows
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for col in range(COLUMNS):
            row_str += f" {board[row][col]} |"
        print(row_str)
    
    # Print bottom border
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col_index):
    """Check if a move is valid (column exists and is not full)."""
    if col_index < 0 or col_index >= COLUMNS:
        return False
    
    # Check if the top row of the column is empty
    return board[0][col_index] == EMPTY_SPACE

def get_next_open_row(board, col_index):
    """Find the lowest available row in the given column."""
    for row in range(ROWS-1, -1, -1):
        if board[row][col_index] == EMPTY_SPACE:
            return row
    return -1  # Column is full (should not happen if is_valid_move is called first)

def make_move(board, col_index, player_symbol):
    """Place the player's symbol in the next available row of the chosen column."""
    row = get_next_open_row(board, col_index)
    board[row][col_index] = player_symbol

def check_win(board, player_symbol):
    """Check if the current player has won."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - CONNECT_COUNT + 1):
            if all(board[row][col + i] == player_symbol for i in range(CONNECT_COUNT)):
                return True
    
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - CONNECT_COUNT + 1):
            if all(board[row + i][col] == player_symbol for i in range(CONNECT_COUNT)):
                return True
    
    # Check diagonal (positive slope)
    for row in range(ROWS - CONNECT_COUNT + 1):
        for col in range(COLUMNS - CONNECT_COUNT + 1):
            if all(board[row + i][col + i] == player_symbol for i in range(CONNECT_COUNT)):
                return True
    
    # Check diagonal (negative slope)
    for row in range(CONNECT_COUNT - 1, ROWS):
        for col in range(COLUMNS - CONNECT_COUNT + 1):
            if all(board[row - i][col + i] == player_symbol for i in range(CONNECT_COUNT)):
                return True
    
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    return all(board[0][col] != EMPTY_SPACE for col in range(COLUMNS))

def get_column_choice(board, player_symbol):
    """Get and validate the player's column choice."""
    valid_columns = "ABCDEFG"
    
    while True:
        try:
            choice = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
            
            if len(choice) != 1 or choice not in valid_columns:
                print("Please enter a single letter between A and G.")
                continue
            
            col_index = valid_columns.index(choice)
            
            if not is_valid_move(board, col_index):
                print("That column is full. Choose another column.")
                continue
            
            return col_index
            
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def main():
    """Main game function."""
    # Create the board
    board = create_board()
    
    # Randomly choose which player goes first
    current_player = random.randint(0, PLAYERS-1)
    
    # Game loop
    game_over = False
    
    # Print initial board
    print_board(board)
    
    while not game_over:
        # Get player's move
        player_symbol = PLAYER_SYMBOLS[current_player]
        col_index = get_column_choice(board, player_symbol)
        
        # Make the move
        make_move(board, col_index, player_symbol)
        
        # Print updated board
        print_board(board)
        
        # Check for win
        if check_win(board, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch players
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()