# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 254
# filename        : gen_0254_sonnet_04.py
# timestamp       : 2026-04-06T10:26:07Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1215
# tokens_total    : 1636
# cost_usd        : 0.019488
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
COLUMN_LETTERS = 'ABCDEFG'

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column labels
    print('   ' + '   '.join(COLUMN_LETTERS))
    
    # Print the board
    for row in range(ROWS):
        print('+---+' * COLS + '+')
        print('|', end='')
        for col in range(COLS):
            print(f' {board[row][col]} |', end='')
        print()
    print('+---+' * COLS + '+')

def is_valid_move(board, col_idx):
    """Check if a move is valid."""
    return board[0][col_idx] == EMPTY

def make_move(board, col_idx, player_symbol):
    """Make a move on the board."""
    # Find the lowest empty row in the selected column
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player_symbol
            return row

def check_win(board, row, col, player_symbol):
    """Check if the current move results in a win."""
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if all(board[row][c+i] == player_symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == player_symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if (r+3 < ROWS and c+3 < COLS and
            all(board[r+i][c+i] == player_symbol for i in range(4))):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(row+3, ROWS-1), max(row, 3)-1, -1), 
                    range(max(0, col-3), min(col+1, COLS-3))):
        if (r-3 >= 0 and c+3 < COLS and
            all(board[r-i][c+i] == player_symbol for i in range(4))):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_player_move(board):
    """Get and validate a player's move."""
    while True:
        try:
            move = input("Enter column (A-G): ").strip().upper()
            
            if len(move) != 1 or move not in COLUMN_LETTERS:
                print("Invalid input. Please enter a letter from A to G.")
                continue
            
            col_idx = COLUMN_LETTERS.index(move)
            
            if not is_valid_move(board, col_idx):
                print("That column is full. Please choose another column.")
                continue
            
            return col_idx
        
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def play_game():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        print(f"Player {player_symbol}'s turn")
        
        col_idx = get_player_move(board)
        row_idx = make_move(board, col_idx, player_symbol)
        
        print_board(board)
        
        if check_win(board, row_idx, col_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()