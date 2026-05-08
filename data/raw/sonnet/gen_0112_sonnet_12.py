# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 112
# filename        : gen_0112_sonnet_12.py
# timestamp       : 2026-04-06T09:55:22Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1082
# tokens_total    : 1500
# cost_usd        : 0.017484
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
COLS = 7
PLAYERS = 2
PLAYER_TOKENS = ['X', 'O']
EMPTY = ' '
CONNECT = 4

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    # Print column headers
    print('   A   B   C   D   E   F   G')
    
    # Print board with rows
    for row in range(ROWS):
        print('+---+---+---+---+---+---+---+')
        row_str = '|'
        for col in range(COLS):
            row_str += f' {board[row][col]} |'
        print(row_str)
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, col_idx):
    return board[0][col_idx] == EMPTY

def make_move(board, col_idx, player_token):
    # Find the lowest empty row in the column
    for row in range(ROWS-1, -1, -1):
        if board[row][col_idx] == EMPTY:
            board[row][col_idx] = player_token
            return row

def check_win(board, row, col, player_token):
    directions = [
        [(0, 1)],             # Horizontal
        [(1, 0)],             # Vertical
        [(1, 1)],             # Diagonal down-right
        [(1, -1)]             # Diagonal down-left
    ]
    
    for direction in directions:
        count = 1  # Count the piece just placed
        
        # Check in the direction
        dr, dc = direction[0]
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_token:
            count += 1
            r += dr
            c += dc
        
        # Check in the opposite direction
        dr, dc = -dr, -dc
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player_token:
            count += 1
            r += dr
            c += dc
        
        if count >= CONNECT:
            return True
    
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == EMPTY:
            return False
    return True

def get_player_move(board, player_token):
    while True:
        try:
            col_letter = input(f"Player {player_token}, choose a column (A-G): ").upper()
            if len(col_letter) != 1 or col_letter < 'A' or col_letter > 'G':
                print("Please enter a letter between A and G.")
                continue
            
            col_idx = ord(col_letter) - ord('A')
            
            if not is_valid_move(board, col_idx):
                print("That column is full. Choose another one.")
                continue
            
            return col_idx
            
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def play_connect4():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    player_token = PLAYER_TOKENS[current_player]
    
    print_board(board)
    
    while True:
        col_idx = get_player_move(board, player_token)
        row = make_move(board, col_idx, player_token)
        print_board(board)
        
        if check_win(board, row, col_idx, player_token):
            print(f"Player {player_token} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = (current_player + 1) % PLAYERS
        player_token = PLAYER_TOKENS[current_player]

if __name__ == "__main__":
    play_connect4()