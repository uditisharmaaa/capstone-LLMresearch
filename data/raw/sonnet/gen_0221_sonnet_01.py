# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 221
# filename        : gen_0221_sonnet_01.py
# timestamp       : 2026-04-06T10:19:21Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1356
# tokens_total    : 1777
# cost_usd        : 0.021603
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
EMPTY = ' '
PLAYER_SYMBOLS = ['X', 'O']
CONNECT_N = 4  # Number of pieces needed to connect for a win

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    
    # Print column labels
    print("   A   B   C   D   E   F   G")
    
    # Print the board
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for col in range(COLUMNS):
            row_str += f" {board[row][col]} |"
        print(row_str)
    
    # Print the bottom border
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col_index):
    # Check if the column is full
    return board[0][col_index] == EMPTY

def get_next_open_row(board, col_index):
    for row in range(ROWS-1, -1, -1):
        if board[row][col_index] == EMPTY:
            return row
    return -1  # Column is full (should not happen with valid moves)

def get_player_move(board, player):
    while True:
        try:
            move = input(f"Player {player + 1} ({PLAYER_SYMBOLS[player]}), choose a column (A-G): ")
            
            # Check if input is a single letter
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter from A to G.")
                continue
                
            # Convert letter to column index (A=0, B=1, etc.)
            col_index = ord(move.upper()) - ord('A')
            
            # Check if column is valid
            if col_index < 0 or col_index >= COLUMNS:
                print("Please enter a letter from A to G.")
                continue
                
            # Check if column is not full
            if not is_valid_move(board, col_index):
                print("That column is full. Choose another column.")
                continue
                
            return col_index
            
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

def check_win(board, row, col, player_symbol):
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLUMNS-3)):
        if all(board[row][c+i] == player_symbol for i in range(4)):
            return True
            
    # Check vertical
    if row <= ROWS - 4:
        if all(board[row+i][col] == player_symbol for i in range(4)):
            return True
            
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                     range(max(0, col-3), min(col+1, COLUMNS-3))):
        if (r+3 < ROWS and c+3 < COLUMNS and 
            all(board[r+i][c+i] == player_symbol for i in range(4))):
            return True
            
    # Check diagonal (up-right)
    for r, c in zip(range(min(row+3, ROWS-1), max(row-1, 2), -1), 
                     range(max(0, col-3), min(col+1, COLUMNS-3))):
        if (r-3 >= 0 and c+3 < COLUMNS and 
            all(board[r-i][c+i] == player_symbol for i in range(4))):
            return True
            
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

def play_game():
    board = create_board()
    game_over = False
    current_player = random.randint(0, NUM_PLAYERS - 1)  # Randomly choose first player
    
    print_board(board)
    
    while not game_over:
        # Get player's move
        col_index = get_player_move(board, current_player)
        
        # Find the next open row in the chosen column
        row_index = get_next_open_row(board, col_index)
        
        # Place the piece
        board[row_index][col_index] = PLAYER_SYMBOLS[current_player]
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row_index, col_index, PLAYER_SYMBOLS[current_player]):
            print(f"Player {current_player + 1} ({PLAYER_SYMBOLS[current_player]}) won!")
            game_over = True
        
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        
        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

def main():
    play_game()

if __name__ == "__main__":
    main()