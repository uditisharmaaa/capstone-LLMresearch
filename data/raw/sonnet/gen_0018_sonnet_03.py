# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 18
# filename        : gen_0018_sonnet_03.py
# timestamp       : 2026-02-19T20:35:33Z
# model           : anthropic/claude-3.5-sonnet
# model_short     : sonnet
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 1133
# tokens_total    : 1548
# cost_usd        : 0.018240
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

import os
import random

# Constants for board dimensions and players
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PIECES = ['X', 'O']
WIN_LENGTH = 4

def create_board():
    """Create empty board with spaces"""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Print current game board with column headers"""
    os.system('clear')
    # Print column headers A-G
    print('   A   B   C   D   E   F   G')
    # Print rows with cell contents
    for row in range(ROWS):
        print('+---' * COLS + '+')
        print('|', end='')
        for col in range(COLS):
            print(f' {board[row][col]} |', end='')
        print()
    print('+---' * COLS + '+')

def is_valid_move(board, col):
    """Check if column choice is valid and not full"""
    # Check if column is within bounds and has empty space
    return 0 <= col < COLS and board[0][col] == EMPTY

def get_next_open_row(board, col):
    """Find lowest empty row in given column"""
    # Check from bottom up for first empty cell
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1

def make_move(board, row, col, piece):
    """Place piece on board at given position"""
    board[row][col] = piece

def check_win(board, piece):
    """Check all possible win conditions"""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS-3):
            if all(board[row][col+i] == piece for i in range(WIN_LENGTH)):
                return True

    # Check vertical
    for row in range(ROWS-3):
        for col in range(COLS):
            if all(board[row+i][col] == piece for i in range(WIN_LENGTH)):
                return True

    # Check diagonal (positive slope)
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if all(board[row+i][col+i] == piece for i in range(WIN_LENGTH)):
                return True

    # Check diagonal (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if all(board[row-i][col+i] == piece for i in range(WIN_LENGTH)):
                return True

    return False

def is_board_full(board):
    """Check if board is completely filled"""
    return all(cell != EMPTY for row in board for cell in row)

def get_player_move(board):
    """Get and validate player column choice"""
    while True:
        try:
            # Get column letter and convert to index
            move = input("Choose column (A-G): ").upper()
            if len(move) != 1 or not 'A' <= move <= 'G':
                print("Please enter a letter A-G")
                continue
            col = ord(move) - ord('A')
            if not is_valid_move(board, col):
                print("Column is full. Choose another.")
                continue
            return col
        except ValueError:
            print("Invalid input. Please enter a letter A-G")

def play_game():
    """Main game loop"""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS-1)
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {PIECES[current_player]}'s turn")
        
        # Get player move and update board
        col = get_player_move(board)
        row = get_next_open_row(board, col)
        make_move(board, row, col, PIECES[current_player])

        # Check win conditions
        if check_win(board, PIECES[current_player]):
            print_board(board)
            print(f"Player {PIECES[current_player]} won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()