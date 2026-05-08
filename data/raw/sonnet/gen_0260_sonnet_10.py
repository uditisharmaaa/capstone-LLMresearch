# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 260
# filename        : gen_0260_sonnet_10.py
# timestamp       : 2026-04-06T10:27:04Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1501
# tokens_total    : 1920
# cost_usd        : 0.023772
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
EMPTY_CELL = ' '
COLUMN_LABELS = 'ABCDEFG'

def create_board():
    """Create a new empty board."""
    return [[EMPTY_CELL for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print top border
    print('+---' * COLS + '+')
    
    # Print rows with cells and borders
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * COLS + '+')

def is_valid_move(board, col_idx):
    """Check if a move is valid."""
    return board[0][col_idx] == EMPTY_CELL

def get_next_open_row(board, col_idx):
    """Find the next open row in the given column."""
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY_CELL:
            return row
    return -1  # Column is full

def drop_checker(board, col_idx, player_symbol):
    """Drop a checker in the specified column."""
    row = get_next_open_row(board, col_idx)
    if row >= 0:
        board[row][col_idx] = player_symbol
        return True
    return False

def check_horizontal_win(board, player_symbol):
    """Check for horizontal win."""
    for row in range(ROWS):
        for col in range(COLS-3):
            if (board[row][col] == player_symbol and 
                board[row][col+1] == player_symbol and 
                board[row][col+2] == player_symbol and 
                board[row][col+3] == player_symbol):
                return True
    return False

def check_vertical_win(board, player_symbol):
    """Check for vertical win."""
    for col in range(COLS):
        for row in range(ROWS-3):
            if (board[row][col] == player_symbol and 
                board[row+1][col] == player_symbol and 
                board[row+2][col] == player_symbol and 
                board[row+3][col] == player_symbol):
                return True
    return False

def check_diagonal_win(board, player_symbol):
    """Check for diagonal win."""
    # Check upward diagonals
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if (board[row][col] == player_symbol and 
                board[row-1][col+1] == player_symbol and 
                board[row-2][col+2] == player_symbol and 
                board[row-3][col+3] == player_symbol):
                return True
    
    # Check downward diagonals
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if (board[row][col] == player_symbol and 
                board[row+1][col+1] == player_symbol and 
                board[row+2][col+2] == player_symbol and 
                board[row+3][col+3] == player_symbol):
                return True
    
    return False

def check_win(board, player_symbol):
    """Check if the player has won."""
    return (check_horizontal_win(board, player_symbol) or 
            check_vertical_win(board, player_symbol) or 
            check_diagonal_win(board, player_symbol))

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != EMPTY_CELL for row in board for cell in row)

def get_player_move(board):
    """Get and validate the player's move."""
    while True:
        try:
            move = input("Choose a column (A-G): ").strip().upper()
            
            # Check if input is a single letter
            if len(move) != 1:
                print("Please enter a single letter.")
                continue
                
            # Check if input is a valid column
            if move not in COLUMN_LABELS:
                print("Please enter a letter between A and G.")
                continue
            
            col_idx = COLUMN_LABELS.index(move)
            
            # Check if the column is full
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another.")
                continue
                
            return col_idx
            
        except Exception as e:
            print(f"Invalid input. Please try again.")

def play_game():
    """Main game loop."""
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)  # Randomly select first player
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        print(f"Player {player_symbol}'s turn")
        col_idx = get_player_move(board)
        
        # Drop the checker
        drop_checker(board, col_idx, player_symbol)
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

def main():
    play_game()

if __name__ == "__main__":
    main()