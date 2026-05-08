# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 455
# filename        : gen_0455_opus_13.py
# timestamp       : 2026-05-07T22:41:47Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 417
# tokens_output   : 1335
# tokens_total    : 1752
# cost_usd        : 0.106380
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

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(ROWS):
        row_list = []
        for col in range(COLS):
            row_list.append(" ")
        board.append(row_list)
    return board

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(COLS):
            print(" " + board[row][col] + " |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_column_from_letter(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2
    elif letter == "D":
        return 3
    elif letter == "E":
        return 4
    elif letter == "F":
        return 5
    elif letter == "G":
        return 6
    else:
        return -1

def is_valid_letter(letter):
    if letter == "A" or letter == "B" or letter == "C" or letter == "D" or letter == "E" or letter == "F" or letter == "G":
        return True
    return False

def is_column_full(board, col):
    if board[0][col] != " ":
        return True
    return False

def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = checker
            return row
    return -1

def check_horizontal(board, checker):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row][col + 1] == checker and board[row][col + 2] == checker and board[row][col + 3] == checker:
                return True
    return False

def check_vertical(board, checker):
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == checker and board[row + 1][col] == checker and board[row + 2][col] == checker and board[row + 3][col] == checker:
                return True
    return False

def check_diagonal(board, checker):
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row + 1][col + 1] == checker and board[row + 2][col + 2] == checker and board[row + 3][col + 3] == checker:
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row - 1][col + 1] == checker and board[row - 2][col + 2] == checker and board[row - 3][col + 3] == checker:
                return True
    return False

def check_win(board, checker):
    if check_horizontal(board, checker):
        return True
    if check_vertical(board, checker):
        return True
    if check_diagonal(board, checker):
        return True
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def get_player_move(board, player_checker):
    while True:
        user_input = input("Player " + player_checker + ", choose a column (A-G): ")
        if len(user_input) != 1:
            print("Invalid input. Please enter a single letter A-G.")
            continue
        letter = user_input.upper()
        if not letter.isalpha():
            print("Invalid input. Please enter a letter A-G.")
            continue
        if not is_valid_letter(letter):
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = get_column_from_letter(letter)
        if is_column_full(board, col):
            print("Column is full. Choose another column.")
            continue
        return col

def main():
    board = create_board()
    players = ["X", "O"]
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        current_checker = players[current_player_index]
        col = get_player_move(board, current_checker)
        drop_checker(board, col, current_checker)
        print_board(board)
        if check_win(board, current_checker):
            print(current_checker + " won!")
            break
        if is_board_full(board):
            print("Draw!")
            break
        current_player_index = (current_player_index + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()