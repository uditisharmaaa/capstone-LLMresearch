# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 239
# filename        : gen_0239_sonnet_04.py
# timestamp       : 2026-04-06T10:23:55Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1307
# tokens_total    : 1728
# cost_usd        : 0.020868
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
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_PIECES = ['X', 'O']
CONNECT_N = 4
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS))
    
    # Print top border
    print('+---' * COLS + '+')
    
    # Print rows with borders
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * COLS + '+')

def is_valid_move(board, col_idx):
    """Check if a move is valid."""
    return board[0][col_idx] == EMPTY

def drop_piece(board, col_idx, piece):
    """Drop a piece in the specified column."""
    # Find the lowest empty row
    for row in range(ROWS - 1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = piece
            return row

def check_win(board, row, col, piece):
    """Check if the last move results in a win."""
    # Check horizontal
    for c in range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1)):
        if all(board[row][c + i] == piece for i in range(CONNECT_N)):
            return True
    
    # Check vertical
    for r in range(max(0, row - CONNECT_N + 1), min(ROWS - CONNECT_N + 1, row + 1)):
        if all(board[r + i][col] == piece for i in range(CONNECT_N)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row - CONNECT_N + 1), min(ROWS - CONNECT_N + 1, row + 1)),
                   range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1))):
        if all(board[r + i][c + i] == piece for i in range(CONNECT_N)):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS - 1, row + CONNECT_N - 1), max(-1, row - 1), -1),
                   range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1))):
        if all(board[r - i][c + i] == piece for i in range(CONNECT_N)):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(board[0][col] != EMPTY for col in range(COLS))

def get_player_move(board):
    """Get a valid move from the player."""
    while True:
        try:
            move = input("Choose a column (A-G): ").upper()
            if len(move) != 1 or move not in COLUMN_LABELS:
                print("Invalid input. Please enter a letter A-G.")
                continue
            
            col_idx = COLUMN_LABELS.index(move)
            if not is_valid_move(board, col_idx):
                print("Column is full. Choose another column.")
                continue
            
            return col_idx
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def play_connect4():
    """Main game function."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    os.system('clear')
    print("Welcome to Connect 4!")
    print("Player 1: X, Player 2: O")
    print_board(board)
    
    while not game_over:
        print(f"Player {current_player + 1}'s turn ({PLAYER_PIECES[current_player]})")
        
        col_idx = get_player_move(board)
        row_idx = drop_piece(board, col_idx, PLAYER_PIECES[current_player])
        
        os.system('clear')
        print_board(board)
        
        if check_win(board, row_idx, col_idx, PLAYER_PIECES[current_player]):
            print(f"Player {current_player + 1} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_connect4()