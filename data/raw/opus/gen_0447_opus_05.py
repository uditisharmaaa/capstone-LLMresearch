# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 447
# filename        : gen_0447_opus_05.py
# timestamp       : 2026-05-07T22:39:12Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 416
# tokens_output   : 1298
# tokens_total    : 1714
# cost_usd        : 0.103590
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

NUM_COLUMNS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2

COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
PLAYERS = ['X', 'O']


def create_board():
    board = []
    for row in range(NUM_ROWS):
        board.append([' '] * NUM_COLUMNS)
    return board


def clear_screen():
    os.system('clear')


def print_board(board):
    clear_screen()
    header = "   " + "   ".join(COLUMN_LABELS)
    print(header)
    separator = "+---" * NUM_COLUMNS + "+"
    for row in range(NUM_ROWS):
        print(separator)
        row_str = "|"
        for col in range(NUM_COLUMNS):
            row_str += " " + board[row][col] + " |"
        print(row_str)
    print(separator)


def get_column_from_input(letter):
    return ord(letter) - ord('A')


def is_valid_column_letter(letter):
    return letter in COLUMN_LABELS


def is_column_full(board, col):
    return board[0][col] != ' '


def get_player_input(board, player):
    while True:
        user_input = input(f"Player {player}, choose a column (A-G): ")
        if len(user_input) != 1:
            print("Invalid input. Please enter a single letter A-G.")
            continue
        letter = user_input.upper()
        if not letter.isalpha():
            print("Invalid input. Please enter a letter A-G.")
            continue
        if not is_valid_column_letter(letter):
            print("Invalid column. Please enter a letter A-G.")
            continue
        col = get_column_from_input(letter)
        if is_column_full(board, col):
            print("Column is full. Choose another column.")
            continue
        return col


def drop_checker(board, col, player):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row
    return -1


def check_horizontal_win(board, player):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS - 3):
            if (board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player):
                return True
    return False


def check_vertical_win(board, player):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLUMNS):
            if (board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player):
                return True
    return False


def check_diagonal_win(board, player):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLUMNS - 3):
            if (board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player):
                return True
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLUMNS - 3):
            if (board[row][col] == player and
                board[row - 1][col + 1] == player and
                board[row - 2][col + 2] == player and
                board[row - 3][col + 3] == player):
                return True
    return False


def check_win(board, player):
    return (check_horizontal_win(board, player) or
            check_vertical_win(board, player) or
            check_diagonal_win(board, player))


def is_board_full(board):
    for col in range(NUM_COLUMNS):
        if board[0][col] == ' ':
            return False
    return True


def select_starting_player():
    return random.randint(0, NUM_PLAYERS - 1)


def play_game():
    board = create_board()
    current_player_index = select_starting_player()
    print_board(board)
    while True:
        current_player = PLAYERS[current_player_index]
        col = get_player_input(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)
        if check_win(board, current_player):
            print(f"{current_player} won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    play_game()