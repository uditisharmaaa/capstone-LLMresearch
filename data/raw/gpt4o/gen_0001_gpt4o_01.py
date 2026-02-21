# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 1
# filename        : gen_0001_gpt4o_01.py
# timestamp       : 2026-02-19T20:28:49Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 765
# tokens_total    : 1156
# cost_usd        : 0.008627
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

ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_column(column):
    return column in "ABCDEFG"

def is_column_full(board, column):
    return all(board[row][column] != ' ' for row in range(ROWS))

def get_column_index(letter):
    return ord(letter) - ord('A')

def get_next_open_row(board, column):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == ' ':
            return row
    return None

def drop_checker(board, column, checker):
    row = get_next_open_row(board, column)
    if row is not None:
        board[row][column] = checker
        return True
    return False

def check_winner(board, checker):
    # Check horizontal locations
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical locations
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

def main():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn. Choose a column (A-G):")
        move = input().strip().upper()

        if is_valid_column(move):
            column = get_column_index(move)
            if not is_column_full(board, column):
                drop_checker(board, column, current_player)

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} won!")
                    game_over = True
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = switch_player(current_player)
            else:
                print("Column is full. Choose another one.")
        else:
            print("Invalid input. Choose a column between A-G.")

if __name__ == "__main__":
    main()