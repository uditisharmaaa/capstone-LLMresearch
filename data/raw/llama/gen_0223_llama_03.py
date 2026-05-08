# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 223
# filename        : gen_0223_llama_03.py
# timestamp       : 2026-04-06T10:19:51Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 390
# tokens_output   : 983
# tokens_total    : 1373
# cost_usd        : 0.000940
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

```python
import os
import random

# Global constants for board dimensions and number of players
BOARD_COLUMNS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Initialize the game board with spaces
board = [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

# Define the players and their corresponding checkers
players = ['X', 'O']

# Randomly select the first player
current_player = random.choice(players)

def print_board():
    # Clear the screen before printing the board
    os.system('clear')
    
    # Print the column labels
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    
    # Print each row of the board
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')
    
    # Print the column labels again
    print('  A   B   C   D   E   F   G')

def is_valid_move(column):
    # Check if the column is within the valid range
    if column < 0 or column >= BOARD_COLUMNS:
        return False
    
    # Check if the column is not full
    if board[0][column]!= ' ':
        return False
    
    return True

def make_move(column):
    # Find the lowest available row in the chosen column
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = current_player
            break

def check_win():
    # Check for horizontal wins
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]!= ' ':
                return True
    
    # Check for vertical wins
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]!= ' ':
                return True
    
    # Check for diagonal wins (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]!= ' ':
                return True
    
    # Check for diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]!= ' ':
                return True
    
    return False

def game_over():
    # Check if the board is full
    if all(cell!= ' ' for row in board for cell in row):
        return True
    
    # Check if a player has won
    if check_win():
        return True
    
    return False

print_board()

while True:
    # Get the player's move
    while True:
        move = input(f"Player {current_player}, choose a column (A-G): ").strip().upper()
        
        # Validate the input
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        column = ord(move) - ord('A')
        
        # Check if the move is valid
        if not is_valid_move(column):
            print("Invalid move. Please choose a different column.")
            continue
        
        break
    
    # Make the move
    make_move(ord(move) - ord('A'))
    
    # Print the updated board
    print_board()
    
    # Check if the game is over
    if game_over():
        # Check if a player has won
        if check_win():
            print(f"Player {current_player} won!")
        else:
            print("It's a draw!")
        break
    
    # Switch to the next player
    current_player = 'O' if current_player == 'X' else 'X'
```