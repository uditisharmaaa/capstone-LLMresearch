# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 185
# filename        : gen_0185_sonnet_10.py
# timestamp       : 2026-04-06T10:12:49Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1293
# tokens_total    : 1712
# cost_usd        : 0.020652
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
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_TOKENS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CONNECT_N = 4  # Number of tokens in a row to win

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS) + '   ')
    
    # Print board
    for row in range(ROWS):
        print('+---' * COLS + '+')
        print('|', end='')
        for col in range(COLS):
            print(f' {board[row][col]} |', end='')
        print()
    
    # Print bottom border
    print('+---' * COLS + '+')

def get_column_choice(player_token):
    """Get and validate column choice from the player."""
    while True:
        choice = input(f"Player {player_token}, choose a column (A-G): ")
        if len(choice) != 1:
            print("Please enter a single letter.")
            continue
        
        if choice not in COLUMN_LABELS:
            print("Please enter a letter between A and G.")
            continue
            
        return COLUMN_LABELS.index(choice)

def is_column_full(board, col):
    """Check if a column is full."""
    return board[0][col] != EMPTY

def drop_token(board, col, token):
    """Drop a token in the specified column."""
    # Find the lowest empty row
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = token
            return row
    return -1  # Column is full, should not happen if validation is done

def check_win(board, row, col, token):
    """Check if the last move resulted in a win."""
    # Check horizontal
    for c in range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1)):
        if all(board[row][c + i] == token for i in range(CONNECT_N)):
            return True
    
    # Check vertical
    for r in range(max(0, row - CONNECT_N + 1), min(ROWS - CONNECT_N + 1, row + 1)):
        if all(board[r + i][col] == token for i in range(CONNECT_N)):
            return True
    
    # Check diagonal (bottom-left to top-right)
    for i in range(-min(row, col, CONNECT_N - 1), min(ROWS - row, COLS - col, CONNECT_N)):
        if i <= -CONNECT_N + 1 or i > 0:
            continue
        if all(board[row + i + j][col + i + j] == token for j in range(CONNECT_N - i)):
            return True
    
    # Check diagonal (top-left to bottom-right)
    for i in range(-min(ROWS - 1 - row, col, CONNECT_N - 1), min(row + 1, COLS - col, CONNECT_N)):
        if i <= -CONNECT_N + 1 or i > 0:
            continue
        if all(board[row - i - j][col + i + j] == token for j in range(CONNECT_N - i)):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        token = PLAYER_TOKENS[current_player]
        
        # Get valid column choice
        while True:
            col = get_column_choice(token)
            if not is_column_full(board, col):
                break
            print("That column is full. Please choose another.")
        
        # Drop token and get the row where it landed
        row = drop_token(board, col, token)
        
        # Print updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, token):
            print(f"Player {token} won!")
            game_over = True
            continue
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            game_over = True
            continue
        
        # Switch players
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()