# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 57
# filename        : gen_0057_gpt4o_12.py
# timestamp       : 2026-02-19T20:48:15Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 390
# tokens_output   : 584
# tokens_total    : 974
# cost_usd        : 0.006815
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

ROWS = 6
COLUMNS = 7
PLAYERS = ['X', 'O']

def clear_screen():
    os.system('clear')

def initialize_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G  ")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def get_column_input():
    while True:
        move = input("Choose a column (A-G): ").strip().upper()
        if move in 'ABCDEFG':
            return ord(move) - ord('A')
        print("Invalid input. Please use a letter from A to G.")

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_checker(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            return

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if (col <= COLUMNS - 4 and all(board[row][col+i] == player for i in range(4)) or
                row <= ROWS - 4 and all(board[row+i][col] == player for i in range(4)) or
                row <= ROWS - 4 and col <= COLUMNS - 4 and all(board[row+i][col+i] == player for i in range(4)) or
                row >= 3 and col <= COLUMNS - 4 and all(board[row-i][col+i] == player for i in range(4))):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def play_game():
    board = initialize_board()
    current_player = random.choice(PLAYERS)
    print_board(board)

    while True:
        print(f"{current_player}'s turn.")
        col = get_column_input()

        if not is_valid_move(board, col):
            print("Column full. Choose another column.")
            continue

        drop_checker(board, col, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} won!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        current_player = PLAYERS[1] if current_player == PLAYERS[0] else PLAYERS[0]

play_game()