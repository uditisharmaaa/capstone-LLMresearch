# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 58
# filename        : gen_0058_gpt4o_13.py
# timestamp       : 2026-02-19T20:48:30Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 387
# tokens_output   : 901
# tokens_total    : 1288
# cost_usd        : 0.009978
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
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

# Initialize the board
def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

# Print the board
def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

# Check if a column is full
def is_column_full(board, col):
    return board[0][col] != ' '

# Get the next open row in the column
def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            return row
    return None

# Place the checker in the board
def place_checker(board, row, col, checker):
    board[row][col] = checker

# Check for a win
def check_for_win(board, checker):
    # Check horizontal locations for win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == checker and board[r][c + 1] == checker and board[r][c + 2] == checker and board[r][c + 3] == checker:
                return True

    # Check vertical locations for win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == checker and board[r + 1][c] == checker and board[r + 2][c] == checker and board[r + 3][c] == checker:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == checker and board[r + 1][c + 1] == checker and board[r + 2][c + 2] == checker and board[r + 3][c + 3] == checker:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == checker and board[r - 1][c + 1] == checker and board[r - 2][c + 2] == checker and board[r - 3][c + 3] == checker:
                return True
    return False

# Check if the board is full
def is_board_full(board):
    for c in range(COLUMNS):
        if board[0][c] == ' ':
            return False
    return True

# Main game loop
def play_game():
    board = create_board()
    print_board(board)
    
    turn = random.randint(0, PLAYERS - 1)
    player_checkers = ['X', 'O']
    
    while True:
        print(f"Player {turn + 1} ({player_checkers[turn]}) turn")
        
        valid_input = False
        while not valid_input:
            col_input = input("Choose a column (A-G): ").strip().upper()
            if col_input in COLUMN_LABELS:
                col = COLUMN_LABELS.index(col_input)
                if not is_column_full(board, col):
                    valid_input = True
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid input. Please enter a letter from A to G.")
        
        row = get_next_open_row(board, col)
        place_checker(board, row, col, player_checkers[turn])
        print_board(board)
        
        if check_for_win(board, player_checkers[turn]):
            print(f"Player {turn + 1} ({player_checkers[turn]}) won!")
            break
        elif is_board_full(board):
            print("The game is a draw!")
            break
        
        turn = (turn + 1) % PLAYERS

play_game()