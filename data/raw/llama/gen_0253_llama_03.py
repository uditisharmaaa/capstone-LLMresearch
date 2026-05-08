# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 253
# filename        : gen_0253_llama_03.py
# timestamp       : 2026-04-06T09:43:08Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 390
# tokens_output   : 894
# tokens_total    : 1284
# cost_usd        : 0.000873
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

# Constant global variables for board dimensions and number of players
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to print the board
def print_board():
    # Clear the screen
    os.system('clear')
    
    # Print column labels
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    
    # Print each row of the board
    for row in board:
        print('|', end='')
        for cell in row:
            print(' ' + cell + ' |', end='')
        print('\n+---+---+---+---+---+---+---+')

# Function to check for a win
def check_win(player):
    # Check horizontal locations for win
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(3, BOARD_ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

# Main game loop
def game():
    # Randomly select which player goes first
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Print the initial board
    print_board()
    
    # Game loop
    while True:
        # Get the current player's move
        while True:
            move = input("Player " + str(current_player + 1) + ", choose a column (A-G): ").upper()
            
            # Validate input
            if move not in 'ABCDEFG':
                print("Invalid input. Please enter a letter between A and G.")
                continue
            
            # Convert column letter to index
            col = ord(move) - ord('A')
            
            # Check if column is full
            if board[0][col]!= ' ':
                print("Column is full. Please choose a different column.")
                continue
            
            # Drop the checker to the lowest available row in the chosen column
            for row in range(BOARD_ROWS - 1, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = 'X' if current_player == 0 else 'O'
                    break
            
            # Print the updated board
            print_board()
            
            # Check for a win
            if check_win('X' if current_player == 0 else 'O'):
                print("Player " + str(current_player + 1) + " won!")
                return
            
            # Check for a draw
            if all(cell!= ' ' for row in board for cell in row):
                print("It's a draw!")
                return
            
            # Switch to the other player
            current_player = (current_player + 1) % NUM_PLAYERS
            break

# Start the game
game()
```