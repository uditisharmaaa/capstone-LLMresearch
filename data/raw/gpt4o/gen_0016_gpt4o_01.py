# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 16
# filename        : gen_0016_gpt4o_01.py
# timestamp       : 2026-02-19T20:34:54Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 682
# tokens_total    : 1073
# cost_usd        : 0.007798
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

# Constants for the board dimensions and number of players
ROWS = 6
COLUMNS = 7
PLAYERS = 2

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def get_column_from_input(input_char):
    return ord(input_char) - ord('A')

def is_valid_input(input_char, board):
    if len(input_char) != 1 or input_char < 'A' or input_char > 'G':
        return False
    column = get_column_from_input(input_char)
    if board[0][column] != ' ':
        return False
    return True

def drop_checker(board, column, checker):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = checker
            break

def check_winner(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS-3):
            if all(board[row][col+i] == checker for i in range(4)):
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS-3):
            if all(board[row+i][col] == checker for i in range(4)):
                return True
    # Check diagonal /
    for row in range(ROWS-3):
        for col in range(COLUMNS-3):
            if all(board[row+i][col+i] == checker for i in range(4)):
                return True
    # Check diagonal \
    for row in range(3, ROWS):
        for col in range(COLUMNS-3):
            if all(board[row-i][col+i] == checker for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice([0, 1])
    print_board(board)

    while True:
        player_checker = players[current_player]
        input_char = input(f"Player {player_checker}, choose a column (A-G): ").strip().upper()
        
        if not is_valid_input(input_char, board):
            print("Invalid input. Please try again.")
            continue
        
        column = get_column_from_input(input_char)
        drop_checker(board, column, player_checker)
        print_board(board)

        if check_winner(board, player_checker):
            print(f"Player {player_checker} won!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

play_game()
