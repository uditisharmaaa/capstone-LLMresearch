# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 189
# filename        : gen_0189_sonnet_14.py
# timestamp       : 2026-04-06T10:13:38Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 416
# tokens_output   : 890
# tokens_total    : 1306
# cost_usd        : 0.014598
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_checker(board, col, symbol):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = symbol
            return row

def check_win(board, row, col, symbol):
    # Check horizontal
    for c in range(COLS-3):
        if all(board[row][c+i] == symbol for i in range(4)):
            return True
    
    # Check vertical
    for r in range(ROWS-3):
        if all(board[r+i][col] == symbol for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i] == symbol for i in range(4)):
                return True
    
    # Check diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i] == symbol for i in range(4)):
                return True
    
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_column_choice(board, player):
    while True:
        try:
            choice = input(f"Player {player}, choose a column (A-G): ")
            if len(choice) != 1 or not choice.isalpha() or choice not in "ABCDEFG":
                print("Invalid input. Please enter a letter A-G.")
                continue
            
            col = ord(choice) - ord('A')
            if not is_valid_move(board, col):
                print("Column is full. Choose another column.")
                continue
            
            return col
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def play_game():
    board = create_board()
    current_player = random.randint(0, PLAYERS-1)
    symbol = PLAYER_SYMBOLS[current_player]
    
    print_board(board)
    
    while True:
        col = get_column_choice(board, symbol)
        row = drop_checker(board, col, symbol)
        print_board(board)
        
        if check_win(board, row, col, symbol):
            print(f"Player {symbol} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS
        symbol = PLAYER_SYMBOLS[current_player]

if __name__ == "__main__":
    play_game()