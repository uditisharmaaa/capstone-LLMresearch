# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 229
# filename        : gen_0229_sonnet_09.py
# timestamp       : 2026-04-06T10:20:54Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 420
# tokens_output   : 1262
# tokens_total    : 1682
# cost_usd        : 0.020190
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
CONNECT = 4  # Number of pieces needed in a row to win

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    # Print column labels
    print('   A   B   C   D   E   F   G')
    
    # Print board
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, column):
    """Check if a move is valid."""
    # Check if the column is within the valid range
    if column < 0 or column >= COLUMNS:
        return False
    
    # Check if the column is full
    return board[0][column] == EMPTY

def make_move(board, column, player_symbol):
    """Place a piece in the specified column."""
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = player_symbol
            return row

def check_win(board, row, column, player_symbol):
    """Check if the current move results in a win."""
    directions = [
        [(0, 1)],  # Horizontal
        [(1, 0)],  # Vertical
        [(1, 1)],  # Diagonal (down-right)
        [(1, -1)]  # Diagonal (down-left)
    ]
    
    for direction in directions:
        count = 1  # Start with 1 for the piece just placed
        
        # Check in the direction
        dx, dy = direction[0]
        for i in range(1, CONNECT):
            r, c = row + i*dx, column + i*dy
            if 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == player_symbol:
                count += 1
            else:
                break
        
        # Check in the opposite direction
        dx, dy = -dx, -dy
        for i in range(1, CONNECT):
            r, c = row + i*dx, column + i*dy
            if 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == player_symbol:
                count += 1
            else:
                break
        
        if count >= CONNECT:
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    for col in range(COLUMNS):
        if board[0][col] == EMPTY:
            return False
    return True

def get_column_choice(board, player):
    """Get a valid column choice from the player."""
    while True:
        try:
            choice = input(f"Player {player + 1} ({PLAYER_SYMBOLS[player]}), choose a column (A-G): ")
            if len(choice) != 1 or not choice.isalpha():
                print("Please enter a single letter.")
                continue
            
            column = ord(choice.upper()) - ord('A')
            
            if column < 0 or column >= COLUMNS:
                print("Please enter a letter between A and G.")
                continue
            
            if not is_valid_move(board, column):
                print("That column is full. Choose another.")
                continue
            
            return column
        
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def play_game():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    print_board(board)
    
    while True:
        # Get the player's move
        column = get_column_choice(board, current_player)
        
        # Make the move
        row = make_move(board, column, PLAYER_SYMBOLS[current_player])
        
        # Print the updated board
        print_board(board)
        
        # Check for a win
        if check_win(board, row, column, PLAYER_SYMBOLS[current_player]):
            print(f"Player {current_player + 1} ({PLAYER_SYMBOLS[current_player]}) won!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch players
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()