# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 225
# filename        : gen_0225_sonnet_05.py
# timestamp       : 2026-04-06T10:20:11Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 416
# tokens_output   : 1377
# tokens_total    : 1793
# cost_usd        : 0.021903
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
#   Write with descriptive function names and minimal comments.
# ====================================================================

import os
import random

# Global constants
NUM_ROWS = 6
NUM_COLS = 7
EMPTY = ' '
PLAYER_PIECES = ['X', 'O']
NUM_PLAYERS = 2
CONNECT_N = 4  # Number of pieces needed in a row to win

def create_board():
    """Create an empty board."""
    return [[EMPTY for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Print the game board with column labels."""
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    
    for row in range(NUM_ROWS):
        print("|", end="")
        for col in range(NUM_COLS):
            print(f" {board[row][col]} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    """Check if a move is valid (column exists and is not full)."""
    if col < 0 or col >= NUM_COLS:
        return False
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    """Find the lowest empty row in the given column."""
    for row in range(NUM_ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1  # Column is full

def drop_piece(board, row, col, piece):
    """Place a piece on the board."""
    board[row][col] = piece

def check_win(board, row, col, piece):
    """Check if the last move resulted in a win."""
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, NUM_COLS-3)):
        if all(board[row][c+i] == piece for i in range(CONNECT_N)):
            return True
            
    # Check vertical
    for r in range(max(0, row-3), min(row+1, NUM_ROWS-3)):
        if all(board[r+i][col] == piece for i in range(CONNECT_N)):
            return True
            
    # Check diagonal (positive slope)
    for r, c in zip(range(row, row-CONNECT_N, -1), range(col-CONNECT_N+1, col+1)):
        if r < 0 or c < 0:
            continue
        if r+CONNECT_N > NUM_ROWS or c+CONNECT_N > NUM_COLS:
            continue
        if all(board[r+i][c+i] == piece for i in range(CONNECT_N)):
            return True
            
    # Check diagonal (negative slope)
    for r, c in zip(range(row, row+CONNECT_N), range(col-CONNECT_N+1, col+1)):
        if r < 0 or c < 0:
            continue
        if r-CONNECT_N+1 < 0 or c+CONNECT_N > NUM_COLS:
            continue
        if all(board[r-i][c+i] == piece for i in range(CONNECT_N)):
            return True
            
    return False

def is_board_full(board):
    """Check if the board is completely filled."""
    return all(board[0][col] != EMPTY for col in range(NUM_COLS))

def get_player_move(board, player_piece):
    """Get and validate a player's move."""
    while True:
        try:
            move = input(f"Player {player_piece}, choose a column (A-G): ").upper()
            if len(move) != 1 or not 'A' <= move <= 'G':
                print("Invalid input. Please enter a letter between A and G.")
                continue
                
            col = ord(move) - ord('A')
            if not is_valid_move(board, col):
                print("Column is full. Choose another column.")
                continue
                
            return col
        except Exception:
            print("Invalid input. Please enter a letter between A and G.")

def play_game():
    """Main game function."""
    board = create_board()
    game_over = False
    
    # Randomly select first player
    current_player = random.randint(0, NUM_PLAYERS-1)
    
    print_board(board)
    
    while not game_over:
        # Get player's move
        col = get_player_move(board, PLAYER_PIECES[current_player])
        
        # Find the next open row in the chosen column
        row = get_next_open_row(board, col)
        
        # Drop the piece
        drop_piece(board, row, col, PLAYER_PIECES[current_player])
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, PLAYER_PIECES[current_player]):
            print(f"Player {PLAYER_PIECES[current_player]} won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch to next player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()