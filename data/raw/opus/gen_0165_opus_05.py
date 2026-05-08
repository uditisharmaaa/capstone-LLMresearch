# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 165
# filename        : gen_0165_opus_05.py
# timestamp       : 2026-04-06T10:09:06Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 416
# tokens_output   : 1250
# tokens_total    : 1666
# cost_usd        : 0.033330
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
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(ROWS):
        board.append([' '] * COLS)
    return board

def clear_screen():
    os.system('clear')

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in range(ROWS):
        print("|", end="")
        for col in range(COLS):
            print(f" {board[row][col]} |", end="")
        print()
        print("+---+---+---+---+---+---+---+")

def get_column_from_letter(letter):
    return ord(letter) - ord('A')

def is_valid_column(board, col):
    return board[0][col] == ' '

def get_next_available_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            return row
    return -1

def drop_checker(board, col, checker):
    row = get_next_available_row(board, col)
    if row != -1:
        board[row][col] = checker
        return row
    return -1

def get_player_input(board, player):
    while True:
        user_input = input(f"Player {player}, choose a column (A-G): ")
        if len(user_input) != 1:
            print("Invalid input. Please enter a single letter A-G.")
            continue
        if not user_input.isalpha():
            print("Invalid input. Please enter a letter A-G.")
            continue
        letter = user_input.upper()
        if letter < 'A' or letter > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = get_column_from_letter(letter)
        if not is_valid_column(board, col):
            print("That column is full. Please choose another column.")
            continue
        return col

def check_horizontal_win(board, checker):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == checker and
                board[row][col + 1] == checker and
                board[row][col + 2] == checker and
                board[row][col + 3] == checker):
                return True
    return False

def check_vertical_win(board, checker):
    for row in range(ROWS - 3):
        for col in range(COLS):
            if (board[row][col] == checker and
                board[row + 1][col] == checker and
                board[row + 2][col] == checker and
                board[row + 3][col] == checker):
                return True
    return False

def check_diagonal_win(board, checker):
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == checker and
                board[row + 1][col + 1] == checker and
                board[row + 2][col + 2] == checker and
                board[row + 3][col + 3] == checker):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == checker and
                board[row - 1][col + 1] == checker and
                board[row - 2][col + 2] == checker and
                board[row - 3][col + 3] == checker):
                return True
    return False

def check_win(board, checker):
    return (check_horizontal_win(board, checker) or
            check_vertical_win(board, checker) or
            check_diagonal_win(board, checker))

def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == ' ':
            return False
    return True

def select_starting_player():
    return random.randint(0, NUM_PLAYERS - 1)

def play_game():
    board = create_board()
    checkers = ['X', 'O']
    current_player = select_starting_player()
    print_board(board)
    while True:
        checker = checkers[current_player]
        col = get_player_input(board, checker)
        drop_checker(board, col, checker)
        print_board(board)
        if check_win(board, checker):
            print(f"{checker} won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()