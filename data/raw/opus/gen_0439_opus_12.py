# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 439
# filename        : gen_0439_opus_12.py
# timestamp       : 2026-05-07T22:35:42Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 1249
# tokens_total    : 1667
# cost_usd        : 0.099945
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
COLS = 7
NUM_PLAYERS = 2


def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]


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


def is_valid_column(col):
    return 0 <= col < COLS


def is_column_full(board, col):
    return board[0][col] != ' '


def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row
    return -1


def check_horizontal(board, row, col, checker):
    count = 0
    for c in range(COLS):
        if board[row][c] == checker:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    return False


def check_vertical(board, row, col, checker):
    count = 0
    for r in range(ROWS):
        if board[r][col] == checker:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    return False


def check_diagonal(board, row, col, checker):
    for start_row in range(ROWS):
        for start_col in range(COLS):
            if start_col + 3 < COLS and start_row + 3 < ROWS:
                if (board[start_row][start_col] == checker and
                    board[start_row + 1][start_col + 1] == checker and
                    board[start_row + 2][start_col + 2] == checker and
                    board[start_row + 3][start_col + 3] == checker):
                    return True
            if start_col + 3 < COLS and start_row - 3 >= 0:
                if (board[start_row][start_col] == checker and
                    board[start_row - 1][start_col + 1] == checker and
                    board[start_row - 2][start_col + 2] == checker and
                    board[start_row - 3][start_col + 3] == checker):
                    return True
    return False


def check_win(board, row, col, checker):
    return (check_horizontal(board, row, col, checker) or
            check_vertical(board, row, col, checker) or
            check_diagonal(board, row, col, checker))


def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == ' ':
            return False
    return True


def get_player_move(board, checker):
    while True:
        user_input = input(f"Player {checker}, enter column (A-G): ")
        
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A-G.")
            continue
        
        letter = user_input.upper()
        
        if letter < 'A' or letter > 'G':
            print("Invalid column. Please enter a letter between A and G.")
            continue
        
        col = get_column_from_letter(letter)
        
        if is_column_full(board, col):
            print("Column is full. Please choose another column.")
            continue
        
        return col


def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    
    print_board(board)
    
    while True:
        current_checker = players[current_player_index]
        
        col = get_player_move(board, current_checker)
        row = drop_checker(board, col, current_checker)
        
        print_board(board)
        
        if check_win(board, row, col, current_checker):
            print(f"{current_checker} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    play_game()