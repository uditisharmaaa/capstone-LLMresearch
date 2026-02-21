# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 93
# filename        : gen_0093_gpt4o_03.py
# timestamp       : 2026-02-19T21:03:59Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 996
# tokens_total    : 1383
# cost_usd        : 0.010927
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

# Constants for the board dimensions and number of players
BOARD_COLUMNS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Characters for the two players
PLAYER_ONE = 'X'
PLAYER_TWO = 'O'

def create_board():
    """Initialize a 2D board with spaces."""
    return [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    """Print the board with the current state."""
    os.system('clear')  # Clear the screen before printing the board
    # Print column labels
    print("   A   B   C   D   E   F   G")
    # Print the board with boundaries
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def is_valid_column(column_input, board):
    """Check if the column input is valid and not full."""
    # Ensure input is within A-G
    if column_input not in "ABCDEFG":
        return False
    # Check if the column is full
    column = ord(column_input) - ord('A')
    return board[0][column] == ' '

def get_player_input(player, board):
    """Prompt the player for a valid column input."""
    while True:
        column_input = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if is_valid_column(column_input, board):
            return ord(column_input) - ord('A')
        else:
            print("Invalid column. Please choose a valid column.")

def drop_checker(board, column, player):
    """Drop the player's checker into the chosen column."""
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player
            break

def check_winner(board, player):
    """Check for a win condition (4 in a row) for the specified player."""
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    # Check vertical
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS - 3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    # Check diagonal (left to right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    # Check diagonal (right to left)
    for row in range(BOARD_ROWS - 3):
        for col in range(3, BOARD_COLUMNS):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                return True
    return False

def is_draw(board):
    """Check if the board is completely filled."""
    return all(board[0][col] != ' ' for col in range(BOARD_COLUMNS))

def connect4_game():
    """Main function to run the Connect 4 game."""
    board = create_board()
    # Randomly select which player goes first
    current_player = random.choice([PLAYER_ONE, PLAYER_TWO])
    
    print_board(board)  # Print the initial empty board

    while True:
        column = get_player_input(current_player, board)  # Get valid column input from the player
        drop_checker(board, column, current_player)  # Drop the checker in the chosen column
        print_board(board)  # Print the updated board
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        
        # Check if the game is a draw
        if is_draw(board):
            print("The game is a draw!")
            break
        
        # Switch player
        current_player = PLAYER_ONE if current_player == PLAYER_TWO else PLAYER_TWO

# Run the Connect 4 game
connect4_game()