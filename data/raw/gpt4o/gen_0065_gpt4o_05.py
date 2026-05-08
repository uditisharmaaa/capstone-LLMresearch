# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 65
# filename        : gen_0065_gpt4o_05.py
# timestamp       : 2026-02-19T20:52:40Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 739
# tokens_total    : 1126
# cost_usd        : 0.008358
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
#   Write with descriptive function names and minimal comments.
# ====================================================================


import os
import random

ROWS = 6
COLUMNS = 7
PLAYERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(input_str):
    return len(input_str) == 1 and 'A' <= input_str <= 'G'

def is_column_full(board, col):
    return board[0][col] != ' '

def get_column_index(column_char):
    return ord(column_char) - ord('A')

def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            return row
    return -1

def drop_checker(board, col, checker):
    row = get_next_open_row(board, col)
    if row != -1:
        board[row][col] = checker
    return row

def check_winner(board, checker):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == checker for i in range(4)):
                return True
    # Check vertical
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if all(board[r+i][c] == checker for i in range(4)):
                return True
    # Check diagonal /
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == checker for i in range(4)):
                return True
    # Check diagonal \
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == checker for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLUMNS))

def play_game():
    board = create_board()
    current_player_index = random.choice([0, 1])
    print_board(board)
    
    while True:
        print(f"Player {PLAYERS[current_player_index]}'s turn.")
        column = input("Choose a column (A-G): ").strip().upper()
        
        if not is_valid_input(column):
            print("Invalid input. Please choose a letter from A to G.")
            continue
        
        col_index = get_column_index(column)
        if is_column_full(board, col_index):
            print("Column is full. Choose another column.")
            continue
        
        drop_checker(board, col_index, PLAYERS[current_player_index])
        print_board(board)
        
        if check_winner(board, PLAYERS[current_player_index]):
            print(f"Player {PLAYERS[current_player_index]} won!")
            break
        
        if is_draw(board):
            print("The game is a draw.")
            break
        
        current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    play_game()
