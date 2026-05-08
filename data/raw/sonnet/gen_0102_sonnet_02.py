# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 102
# filename        : gen_0102_sonnet_02.py
# timestamp       : 2026-04-06T09:52:56Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 418
# tokens_output   : 985
# tokens_total    : 1403
# cost_usd        : 0.016029
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

ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER_PIECES = ['X', 'O']
EMPTY = ' '
CONNECT = 4

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

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
    return board[0][col] == EMPTY

def drop_piece(board, col, piece):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return row

def check_win(board, row, col, piece):
    # Check horizontal
    for c in range(max(0, col-3), min(col+1, COLS-3)):
        if all(board[row][c+i] == piece for i in range(4)):
            return True
    
    # Check vertical
    if row <= ROWS-4:
        if all(board[row+i][col] == piece for i in range(4)):
            return True
    
    # Check diagonal (down-right)
    for r, c in zip(range(max(0, row-3), min(row+1, ROWS-3)), range(max(0, col-3), min(col+1, COLS-3))):
        if all(board[r+i][c+i] == piece for i in range(4)):
            return True
    
    # Check diagonal (up-right)
    for r, c in zip(range(min(row+3, ROWS-1), max(row-1, 2), -1), range(max(0, col-3), min(col+1, COLS-3))):
        if all(board[r-i][c+i] == piece for i in range(4)):
            return True
    
    return False

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_valid_column(board):
    while True:
        try:
            move = input("Enter column (A-G): ")
            if len(move) != 1 or not move.isalpha():
                print("Please enter a single letter.")
                continue
            
            col = ord(move.upper()) - ord('A')
            if col < 0 or col >= COLS:
                print("Please enter a letter between A and G.")
                continue
            
            if not is_valid_move(board, col):
                print("That column is full. Try another one.")
                continue
            
            return col
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def main():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS-1)
    print_board(board)
    
    while True:
        piece = PLAYER_PIECES[current_player]
        print(f"Player {piece}'s turn")
        
        col = get_valid_column(board)
        row = drop_piece(board, col, piece)
        print_board(board)
        
        if check_win(board, row, col, piece):
            print(f"Player {piece} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()