# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 251
# filename        : gen_0251_sonnet_01.py
# timestamp       : 2026-04-06T10:25:44Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1244
# tokens_total    : 1665
# cost_usd        : 0.019923
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
PLAYER_SYMBOLS = ["X", "O"]
EMPTY = " "
CONNECT = 4  # Number of pieces in a row needed to win

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    # Print column headers
    print("   A   B   C   D   E   F   G")
    
    # Print board
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_display = "|"
        for col in range(COLUMNS):
            row_display += f" {board[row][col]} |"
        print(row_display)
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, column):
    # Check if the column is within range and not full
    return 0 <= column < COLUMNS and board[0][column] == EMPTY

def make_move(board, column, player_symbol):
    # Start from the bottom row and find the first empty cell
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = player_symbol
            return row  # Return the row where the piece was placed

def check_win(board, row, col, player_symbol):
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLUMNS-3)):
        if all(board[row][c+i] == player_symbol for i in range(CONNECT)):
            return True
            
    # Check vertical
    if row <= ROWS - CONNECT:
        if all(board[row+i][col] == player_symbol for i in range(CONNECT)):
            return True
            
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), 
                    range(max(0, col-3), min(col+1, COLUMNS-3))):
        if (r+3 < ROWS and c+3 < COLUMNS and 
            all(board[r+i][c+i] == player_symbol for i in range(CONNECT))):
            return True
            
    # Check diagonal (up-right)
    for r, c in zip(range(min(ROWS-1, row+3), max(row, CONNECT-1) - 1, -1), 
                    range(max(0, col-3), min(col+1, COLUMNS-3))):
        if (r-3 >= 0 and c+3 < COLUMNS and 
            all(board[r-i][c+i] == player_symbol for i in range(CONNECT))):
            return True
            
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))

def column_letter_to_index(letter):
    try:
        column_index = ord(letter) - ord('A')
        if 0 <= column_index < COLUMNS:
            return column_index
        return None
    except:
        return None

def main():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS-1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        # Get player move
        valid_move = False
        while not valid_move:
            try:
                column_letter = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
                column = column_letter_to_index(column_letter)
                
                if column is None:
                    print("Invalid input! Please enter a letter A-G.")
                    continue
                    
                if not is_valid_move(board, column):
                    print("Column is full! Choose another column.")
                    continue
                    
                valid_move = True
            except:
                print("Invalid input! Please enter a letter A-G.")
        
        # Make the move
        row = make_move(board, column, player_symbol)
        
        # Print the updated board
        print_board(board)
        
        # Check for win
        if check_win(board, row, column, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        # Check for draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch to the next player
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()