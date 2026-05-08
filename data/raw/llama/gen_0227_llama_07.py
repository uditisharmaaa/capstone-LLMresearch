# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 227
# filename        : gen_0227_llama_07.py
# timestamp       : 2026-04-06T09:36:14Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 395
# tokens_output   : 915
# tokens_total    : 1310
# cost_usd        : 0.000892
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

```python
import os
import random

# Global constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board():
    # Clear the screen
    os.system('clear')
    
    # Print column labels
    print('  A   B   C   D   E   F   G')
    
    # Print the board
    for row in range(BOARD_HEIGHT):
        print('+---' * BOARD_WIDTH + '+')
        print('|', end='')
        for col in range(BOARD_WIDTH):
            print(f' {board[row][col]} |', end='')
        print()
    print('+---' * BOARD_WIDTH + '+')

def validate_input(player, input_col):
    # Check if input is a letter
    if not input_col.isalpha():
        print("Invalid input. Please enter a letter.")
        return False
    
    # Check if input is within A-G
    if input_col not in 'ABCDEFG':
        print("Invalid input. Please enter a letter between A and G.")
        return False
    
    # Convert input to column index
    col = ord(input_col.upper()) - ord('A')
    
    # Check if column is full
    if board[0][col]!= ' ':
        print("Column is full. Please choose another column.")
        return False
    
    return col

def drop_checker(player, col):
    # Start from the bottom of the column and move up
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return

def check_win(player):
    # Check horizontal
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True
    
    # Check vertical
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True
    
    return False

def main():
    # Randomly select which player goes first
    current_player = random.choice(['X', 'O'])
    
    while True:
        print_board()
        
        # Get player input
        while True:
            input_col = input(f"Player {current_player}, choose a column: ")
            col = validate_input(current_player, input_col)
            if col is not False:
                break
        
        # Drop the checker
        drop_checker(current_player, col)
        
        # Check for a win
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} won!")
            break
        
        # Check for a draw
        if all(board[0][col]!= ' ' for col in range(BOARD_WIDTH)):
            print_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
```