# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 172
# filename        : gen_0172_sonnet_12.py
# timestamp       : 2026-04-06T10:10:21Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1007
# tokens_total    : 1425
# cost_usd        : 0.016359
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_TOKENS = ['X', 'O']
EMPTY = ' '
CONNECT = 4

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print board
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
    print('+---+---+---+---+---+---+---+')

def get_column_choice():
    while True:
        choice = input("Choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Please enter a single letter.")
            continue
        
        if choice not in 'ABCDEFG':
            print("Please enter a letter between A and G.")
            continue
        
        return ord(choice) - ord('A')  # Convert letter to column index

def is_column_full(board, col):
    return board[0][col] != EMPTY

def drop_checker(board, col, token):
    # Start from the bottom row and move up
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = token
            return row
    return -1  # Column is full

def check_win(board, row, col, token):
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal down-right
        [(1, -1)]             # Diagonal down-left
    ]
    
    for direction in directions:
        dx, dy = direction[0]
        count = 1  # Start with 1 for the piece just placed
        
        # Check in both positive and negative directions
        for factor in [1, -1]:
            new_dx, new_dy = dx * factor, dy * factor
            r, c = row + new_dx, col + new_dy
            
            while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == token:
                count += 1
                r += new_dx
                c += new_dy
                
                if count >= CONNECT:
                    return True
        
        if count >= CONNECT:
            return True
    
    return False

def is_board_full(board):
    for col in range(COLUMNS):
        if not is_column_full(board, col):
            return False
    return True

def play_game():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    
    print_board(board)
    
    while True:
        token = PLAYER_TOKENS[current_player]
        print(f"Player {token}'s turn")
        
        # Get valid move
        while True:
            col = get_column_choice()
            
            if is_column_full(board, col):
                print("That column is full. Choose another column.")
                continue
            
            break
        
        # Drop the checker
        row = drop_checker(board, col, token)
        print_board(board)
        
        # Check for win
        if check_win(board, row, col, token):
            print(f"Player {token} won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    play_game()