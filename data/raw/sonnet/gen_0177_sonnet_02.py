# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 177
# filename        : gen_0177_sonnet_02.py
# timestamp       : 2026-04-06T10:11:24Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 418
# tokens_output   : 1077
# tokens_total    : 1495
# cost_usd        : 0.017409
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

import os
import random

# Constants
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = 'ABCDEFG'
EMPTY_CELL = ' '

def create_board():
    return [[EMPTY_CELL for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * NUM_COLS + '+')
    
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * NUM_COLS + '+')

def is_valid_move(board, col_idx):
    return 0 <= col_idx < NUM_COLS and board[0][col_idx] == EMPTY_CELL

def drop_checker(board, col_idx, player_symbol):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_idx] == EMPTY_CELL:
            board[row][col_idx] = player_symbol
            return row

def check_win(board, row, col, player_symbol):
    # Check horizontal
    for c in range(max(0, col - 3), min(col + 1, NUM_COLS - 3)):
        if all(board[row][c+i] == player_symbol for i in range(4)):
            return True
    
    # Check vertical
    if row <= NUM_ROWS - 4:
        if all(board[row+i][col] == player_symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row - 3), min(row + 1, NUM_ROWS - 3)), 
                    range(max(0, col - 3), min(col + 1, NUM_COLS - 3))):
        if all(board[r+i][c+i] == player_symbol for i in range(4)):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(NUM_ROWS - 1, row + 3), max(row - 1, 2), -1), 
                    range(max(0, col - 3), min(col + 1, NUM_COLS - 3))):
        if all(board[r-i][c+i] == player_symbol for i in range(4)):
            return True
    
    return False

def is_board_full(board):
    return all(cell != EMPTY_CELL for row in board for cell in row)

def main():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        while True:
            try:
                user_input = input(f"Player {player_symbol}, choose a column (A-G): ").upper()
                if len(user_input) != 1 or user_input not in COLUMN_LABELS:
                    print("Invalid input. Please enter a letter between A and G.")
                    continue
                
                col_idx = COLUMN_LABELS.index(user_input)
                
                if not is_valid_move(board, col_idx):
                    print("Column is full. Choose another column.")
                    continue
                
                break
            except ValueError:
                print("Invalid input. Please enter a letter between A and G.")
        
        row = drop_checker(board, col_idx, player_symbol)
        print_board(board)
        
        if check_win(board, row, col_idx, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()