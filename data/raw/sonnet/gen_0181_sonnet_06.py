# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 181
# filename        : gen_0181_sonnet_06.py
# timestamp       : 2026-04-06T10:12:20Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 419
# tokens_output   : 966
# tokens_total    : 1385
# cost_usd        : 0.015747
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

import os
import random

# Constants
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
EMPTY = ' '
CONNECT = 4

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    return board[0][col] == EMPTY

def get_valid_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, choose a column (A-G): ").upper()
            if len(move) != 1 or move < 'A' or move > 'G':
                print("Please enter a letter between A and G.")
                continue
            
            col = ord(move) - ord('A')
            if not is_valid_move(board, col):
                print("That column is full. Choose another.")
                continue
                
            return col
        except:
            print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row

def check_win(board, row, col, player):
    # Check horizontal
    for c in range(COLS - CONNECT + 1):
        if all(board[row][c+i] == player for i in range(CONNECT)):
            return True
            
    # Check vertical
    for r in range(ROWS - CONNECT + 1):
        if all(board[r+i][col] == player for i in range(CONNECT)):
            return True
            
    # Check diagonal (down-right)
    for r in range(ROWS - CONNECT + 1):
        for c in range(COLS - CONNECT + 1):
            if all(board[r+i][c+i] == player for i in range(CONNECT)):
                return True
                
    # Check diagonal (up-right)
    for r in range(CONNECT - 1, ROWS):
        for c in range(COLS - CONNECT + 1):
            if all(board[r-i][c+i] == player for i in range(CONNECT)):
                return True
                
    return False

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = create_board()
    current_player_idx = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        current_player = PLAYER_SYMBOLS[current_player_idx]
        
        col = get_valid_move(board, current_player)
        row = drop_checker(board, col, current_player)
        
        print_board(board)
        
        if check_win(board, row, col, current_player):
            print(f"Player {current_player} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player_idx = (current_player_idx + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()