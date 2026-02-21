# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 28
# filename        : gen_0028_gpt4o_13.py
# timestamp       : 2026-02-19T20:41:46Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 387
# tokens_output   : 686
# tokens_total    : 1073
# cost_usd        : 0.007828
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

import os
import random

# Constants
NUM_ROWS = 6
NUM_COLS = 7
PLAYERS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * NUM_COLS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * NUM_COLS + '+')

def get_column_index(column_letter):
    if column_letter in COLUMN_LABELS:
        return COLUMN_LABELS.index(column_letter)
    return -1

def is_valid_column(column_index, board):
    return 0 <= column_index < NUM_COLS and board[0][column_index] == ' '

def drop_checker(board, column_index, player):
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = player
            return

def check_winner(board, player):
    # Check horizontal
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if all(board[r][c+i] == player for i in range(4)):
                return True
    # Check vertical
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS - 3):
            if all(board[r+i][c] == player for i in range(4)):
                return True
    # Check / diagonal
    for r in range(3, NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if all(board[r-i][c+i] == player for i in range(4)):
                return True
    # Check \ diagonal
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if all(board[r+i][c+i] == player for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][c] != ' ' for c in range(NUM_COLS))

def main():
    board = create_board()
    current_player = random.choice(PLAYERS)
    print_board(board)
    
    while True:
        move = input(f"Player {current_player}, choose a column (A-G): ").strip().upper()
        column_index = get_column_index(move)
        
        if column_index == -1 or not is_valid_column(column_index, board):
            print("Invalid move. Try again.")
            continue
        
        drop_checker(board, column_index, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        
        if is_board_full(board):
            print("The game is a draw!")
            break
        
        current_player = PLAYERS[1] if current_player == PLAYERS[0] else PLAYERS[0]

if __name__ == "__main__":
    main()