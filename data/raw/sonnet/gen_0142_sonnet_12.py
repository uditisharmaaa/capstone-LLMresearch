# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 142
# filename        : gen_0142_sonnet_12.py
# timestamp       : 2026-04-06T10:04:07Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1323
# tokens_total    : 1741
# cost_usd        : 0.021099
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
NUM_PLAYERS = 2
EMPTY = ' '
PLAYERS = ['X', 'O']
CONNECT_N = 4  # Number in a row to win

def create_board():
    """Create an empty Connect 4 board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print board with rows
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def get_column_index(column_letter):
    """Convert column letter (A-G) to column index (0-6)."""
    try:
        if not column_letter.isalpha():
            return None
        
        col_index = ord(column_letter.upper()) - ord('A')
        if 0 <= col_index < COLS:
            return col_index
        return None
    except:
        return None

def is_valid_move(board, col_index):
    """Check if a move is valid (column exists and isn't full)."""
    if col_index is None:
        return False
    
    # Check if the top cell in the column is empty
    return board[0][col_index] == EMPTY

def drop_checker(board, col_index, player):
    """Drop a checker into the specified column."""
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][col_index] == EMPTY:
            board[row][col_index] = player
            return row
    return -1  # Should never happen if is_valid_move is checked first

def check_win(board, row, col, player):
    """Check if the last move resulted in a win."""
    directions = [
        [(0, 1), (0, -1)],  # Horizontal
        [(1, 0), (-1, 0)],  # Vertical
        [(1, 1), (-1, -1)],  # Diagonal /
        [(1, -1), (-1, 1)]   # Diagonal \
    ]
    
    for direction_pair in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in both directions
        for dr, dc in direction_pair:
            r, c = row, col
            
            # Count consecutive pieces in this direction
            for _ in range(CONNECT_N - 1):
                r += dr
                c += dc
                
                if (0 <= r < ROWS and 0 <= c < COLS and 
                    board[r][c] == player):
                    count += 1
                else:
                    break
            
            if count >= CONNECT_N:
                return True
        
        if count >= CONNECT_N:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    return all(cell != EMPTY for row in board for cell in row)

def get_player_move(board, player):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {player}, choose a column (A-G): ")
            col_index = get_column_index(move)
            
            if col_index is None:
                print("Invalid column. Please enter a letter from A to G.")
                continue
            
            if not is_valid_move(board, col_index):
                print("That column is full. Choose another column.")
                continue
            
            return col_index
            
        except Exception as e:
            print(f"Invalid input: {e}")

def play_connect4():
    """Main function to play Connect 4."""
    board = create_board()
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    current_player = PLAYERS[current_player_index]
    
    print_board(board)
    
    while True:
        # Get player's move
        col_index = get_player_move(board, current_player)
        
        # Drop the checker and get the row where it landed
        row = drop_checker(board, col_index, current_player)
        
        # Print updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col_index, current_player):
            print(f"{current_player} won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch players
        current_player_index = (current_player_index + 1) % NUM_PLAYERS
        current_player = PLAYERS[current_player_index]

if __name__ == "__main__":
    play_connect4()