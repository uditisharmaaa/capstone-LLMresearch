# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 131
# filename        : gen_0131_gpt4mini_01.py
# timestamp       : 2026-04-06T09:07:12Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 660
# tokens_total    : 1051
# cost_usd        : 0.000455
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

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_COUNT = 2

def create_board():
    return [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print('|' + '|'.join(row) + '|')
        print("+---+---+---+---+---+---+---+")

def drop_checker(board, column, checker):
    for row in reversed(range(ROW_COUNT)):
        if board[row][column] == ' ':
            board[row][column] = checker
            return True
    return False

def is_winning_move(board, checker):
    # Check horizontal
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r][c + i] == checker for i in range(4)):
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == checker for i in range(4)):
                return True

    # Check diagonal (positive slope)
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r + i][c + i] == checker for i in range(4)):
                return True

    # Check diagonal (negative slope)
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r - i][c + i] == checker for i in range(4)):
                return True

    return False

def is_full(board):
    return all(board[0][c] != ' ' for c in range(COLUMN_COUNT))

def main():
    board = create_board()
    players = ['X', 'O']
    current_player_index = random.randint(0, 1)
    current_player = players[current_player_index]

    print_board(board)

    while True:
        column_input = input(f"Player {current_player}, choose a column (A-G): ").upper()
        
        if column_input not in 'ABCDEFG':
            print("Invalid input. Please choose a letter from A to G.")
            continue
        
        column = ord(column_input) - ord('A')
        
        if board[0][column] != ' ':
            print("Column is full. Please choose another column.")
            continue
        
        drop_checker(board, column, current_player)
        print_board(board)

        if is_winning_move(board, current_player):
            print(f"Player {current_player} won!")
            break

        if is_full(board):
            print("It's a draw!")
            break
        
        current_player_index = (current_player_index + 1) % PLAYER_COUNT
        current_player = players[current_player_index]

if __name__ == "__main__":
    main()