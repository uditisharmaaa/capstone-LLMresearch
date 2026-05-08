# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 263
# filename        : gen_0263_sonnet_13.py
# timestamp       : 2026-04-06T10:27:30Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 417
# tokens_output   : 1331
# tokens_total    : 1748
# cost_usd        : 0.021216
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER_PIECES = ['X', 'O']
EMPTY_SPACE = ' '
CONNECT_N = 4  # Number of pieces needed in a row to win

def initialize_board():
    """Initialize an empty board."""
    return [[EMPTY_SPACE for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print the current state of the board."""
    os.system('clear')
    
    # Print column headers (A-G)
    print("   A   B   C   D   E   F   G")
    
    # Print board with pieces
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    """Check if a move is valid."""
    # Check if the column is in range
    if col < 0 or col >= COLS:
        return False
    
    # Check if the column is not full
    return board[0][col] == EMPTY_SPACE

def make_move(board, col, player_piece):
    """Make a move on the board."""
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY_SPACE:
            board[row][col] = player_piece
            return row

def check_win(board, row, col, player_piece):
    """Check if the current move results in a win."""
    # Check horizontal
    for c in range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1)):
        if all(board[row][c + i] == player_piece for i in range(CONNECT_N)):
            return True
    
    # Check vertical
    if row <= ROWS - CONNECT_N:
        if all(board[row + i][col] == player_piece for i in range(CONNECT_N)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row - CONNECT_N + 1), min(ROWS - CONNECT_N + 1, row + 1)),
                   range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1))):
        if all(board[r + i][c + i] == player_piece for i in range(CONNECT_N)):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS - 1, row + CONNECT_N - 1), max(CONNECT_N - 2, row - 1), -1),
                   range(max(0, col - CONNECT_N + 1), min(COLS - CONNECT_N + 1, col + 1))):
        if all(board[r - i][c + i] == player_piece for i in range(CONNECT_N)):
            return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != EMPTY_SPACE for row in board for cell in row)

def get_player_move(board):
    """Get a valid move from the player."""
    while True:
        try:
            move = input("Enter column (A-G): ").strip().upper()
            if len(move) != 1 or not 'A' <= move <= 'G':
                print("Invalid input! Please enter a letter from A to G.")
                continue
            
            col = ord(move) - ord('A')
            if not is_valid_move(board, col):
                print("Column is full! Choose another column.")
                continue
            
            return col
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def main():
    """Main game function."""
    board = initialize_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    print(f"Player {PLAYER_PIECES[current_player]} goes first!")
    
    while not game_over:
        print(f"Player {PLAYER_PIECES[current_player]}'s turn")
        col = get_player_move(board)
        row = make_move(board, col, PLAYER_PIECES[current_player])
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, PLAYER_PIECES[current_player]):
            print(f"Player {PLAYER_PIECES[current_player]} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()