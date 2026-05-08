# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 443
# filename        : gen_0443_opus_01.py
# timestamp       : 2026-05-07T22:36:36Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1182
# tokens_total    : 1603
# cost_usd        : 0.094965
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
COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(ROWS):
        new_row = []
        for col in range(COLS):
            new_row.append(" ")
        board.append(new_row)
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

def get_column_choice(board, player):
    valid_columns = ["A", "B", "C", "D", "E", "F", "G"]
    while True:
        choice = input("Player " + player + ", choose a column (A-G): ")
        if len(choice) != 1:
            print("Invalid input. Please enter a single letter A-G.")
            continue
        choice = choice.upper()
        if choice not in valid_columns:
            print("Invalid input. Please enter a letter A-G.")
            continue
        col_index = ord(choice) - ord("A")
        if board[0][col_index] != " ":
            print("Column " + choice + " is full. Choose another column.")
            continue
        return col_index

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return row
    return -1

def check_horizontal(board, row, col, player):
    count = 0
    for c in range(COLS):
        if board[row][c] == player:
            count = count + 1
            if count >= 4:
                return True
        else:
            count = 0
    return False

def check_vertical(board, row, col, player):
    count = 0
    for r in range(ROWS):
        if board[r][col] == player:
            count = count + 1
            if count >= 4:
                return True
        else:
            count = 0
    return False

def check_diagonal_down_right(board, player):
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == player:
                if board[row + 1][col + 1] == player:
                    if board[row + 2][col + 2] == player:
                        if board[row + 3][col + 3] == player:
                            return True
    return False

def check_diagonal_up_right(board, player):
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == player:
                if board[row - 1][col + 1] == player:
                    if board[row - 2][col + 2] == player:
                        if board[row - 3][col + 3] == player:
                            return True
    return False

def check_winner(board, row, col, player):
    if check_horizontal(board, row, col, player):
        return True
    if check_vertical(board, row, col, player):
        return True
    if check_diagonal_down_right(board, player):
        return True
    if check_diagonal_up_right(board, player):
        return True
    return False

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def play_game():
    board = create_board()
    players = ["X", "O"]
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        current_player = players[current_player_index]
        col = get_column_choice(board, current_player)
        row = drop_checker(board, col, current_player)
        print_board(board)
        if check_winner(board, row, col, current_player):
            print(current_player + " won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current_player_index = (current_player_index + 1) % NUM_PLAYERS

play_game()