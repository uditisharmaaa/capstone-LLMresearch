# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 72
# filename        : gen_0072_gpt4o_12.py
# timestamp       : 2026-02-19T20:59:44Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 390
# tokens_output   : 680
# tokens_total    : 1070
# cost_usd        : 0.007775
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
BOARD_ROWS = 6
BOARD_COLS = 7
PLAYERS = ['X', 'O']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_column(column, board):
    return 0 <= column < BOARD_COLS and board[0][column] == ' '

def get_column_choice():
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if len(choice) == 1 and 'A' <= choice <= 'G':
            return ord(choice) - ord('A')
        print("Invalid input. Please enter a letter from A to G.")

def drop_checker(board, column, checker):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = checker
            return

def check_winner(board, checker):
    # Horizontal check
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True
    # Vertical check
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True
    # Diagonal checks
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True
        for col in range(3, BOARD_COLS):
            if all(board[row + i][col - i] == checker for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(BOARD_COLS))

def connect_4():
    board = create_board()
    current_player = random.choice(PLAYERS)
    
    while True:
        print_board(board)
        print(f"{current_player}'s turn.")
        
        column = get_column_choice()
        while not is_valid_column(column, board):
            print("Column is full or invalid. Choose another.")
            column = get_column_choice()
        
        drop_checker(board, column, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} won!")
            return
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return
        
        current_player = PLAYERS[(PLAYERS.index(current_player) + 1) % len(PLAYERS)]

connect_4()