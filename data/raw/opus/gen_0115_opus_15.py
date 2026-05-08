# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 115
# filename        : gen_0115_opus_15.py
# timestamp       : 2026-04-06T09:56:04Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 418
# tokens_output   : 967
# tokens_total    : 1385
# cost_usd        : 0.026265
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
#   Write in a straightforward, no-frills style.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(ROWS):
        board.append([' '] * COLS)
    return board

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in range(ROWS):
        line = "|"
        for col in range(COLS):
            line += " " + board[row][col] + " |"
        print(line)
        print("+---+---+---+---+---+---+---+")

def get_column(board, player):
    while True:
        user_input = input(f"Player {player}, choose a column (A-G): ")
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A-G.")
            continue
        user_input = user_input.upper()
        if user_input < 'A' or user_input > 'G':
            print("Invalid column. Please enter a letter A-G.")
            continue
        col = ord(user_input) - ord('A')
        if board[0][col] != ' ':
            print("Column is full. Choose another column.")
            continue
        return col

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row
    return -1

def check_win(board, player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == ' ':
            return False
    return True

def main():
    board = create_board()
    players = ['X', 'O']
    current_player = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        player = players[current_player]
        col = get_column(board, player)
        drop_checker(board, col, player)
        print_board(board)
        if check_win(board, player):
            print(f"{player} won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()