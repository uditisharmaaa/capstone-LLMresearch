# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 50
# filename        : gen_0050_gpt4mini_05.py
# timestamp       : 2026-02-19T20:47:01Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 745
# tokens_total    : 1132
# cost_usd        : 0.000505
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
COLS = 7
PLAYERS = 2

def initialize_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_column_full(board, col):
    return board[0][col] != ' '

def drop_checker(board, col, checker):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = checker
            return

def is_winner(board, checker):
    return (check_horizontal(board, checker) or
            check_vertical(board, checker) or
            check_diagonal(board, checker))

def check_horizontal(board, checker):
    for row in board:
        count = 0
        for cell in row:
            count = count + 1 if cell == checker else 0
            if count >= 4:
                return True
    return False

def check_vertical(board, checker):
    for col in range(COLS):
        count = 0
        for row in range(ROWS):
            count = count + 1 if board[row][col] == checker else 0
            if count >= 4:
                return True
    return False

def check_diagonal(board, checker):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == checker:
                if check_diagonal_right(board, row, col, checker) or check_diagonal_left(board, row, col, checker):
                    return True
    return False

def check_diagonal_right(board, row, col, checker):
    if row + 3 < ROWS and col + 3 < COLS:
        return all(board[row + i][col + i] == checker for i in range(4))
    return False

def check_diagonal_left(board, row, col, checker):
    if row + 3 < ROWS and col - 3 >= 0:
        return all(board[row + i][col - i] == checker for i in range(4))
    return False

def is_draw(board):
    return all(is_column_full(board, col) for col in range(COLS))

def get_valid_column():
    while True:
        column = input("Choose a column (A-G): ").upper()
        if column in "ABCDEFG":
            return ord(column) - ord('A')
        print("Invalid input. Please enter a letter between A and G.")

def main():
    board = initialize_board()
    current_player = random.choice(['X', 'O'])
    print_board(board)
    
    while True:
        col = get_valid_column()
        
        while is_column_full(board, col):
            print("Column full! Choose another column.")
            col = get_valid_column()

        drop_checker(board, col, current_player)
        print_board(board)

        if is_winner(board, current_player):
            print(f"{current_player} won!")
            break
        
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()