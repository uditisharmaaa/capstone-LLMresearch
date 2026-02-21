# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 39
# filename        : gen_0039_gpt4o_09.py
# timestamp       : 2026-02-19T20:44:35Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 391
# tokens_output   : 731
# tokens_total    : 1122
# cost_usd        : 0.008287
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

import os
import random

# Constants
BOARD_ROWS = 6
BOARD_COLUMNS = 7
NUM_PLAYERS = 2
PLAYER_CHARS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * BOARD_COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * BOARD_COLUMNS + '+')

def get_column_index(column_letter):
    if column_letter in COLUMN_LABELS:
        return COLUMN_LABELS.index(column_letter)
    return -1

def is_valid_column(column, board):
    if 0 <= column < BOARD_COLUMNS:
        return board[0][column] == ' '
    return False

def drop_checker(board, column, checker):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = checker
            break

def check_winner(board, checker):
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row][col+i] == checker for i in range(4)):
                return True
    # Check vertical
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS):
            if all(board[row+i][col] == checker for i in range(4)):
                return True
    # Check diagonal /
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row-i][col+i] == checker for i in range(4)):
                return True
    # Check diagonal \
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLUMNS - 3):
            if all(board[row+i][col+i] == checker for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = create_board()
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    game_over = False

    while not game_over:
        print_board(board)
        current_player = PLAYER_CHARS[current_player_index]
        valid_move = False

        while not valid_move:
            move = input(f"Player {current_player}, choose a column (A-G): ").strip()
            column_index = get_column_index(move)
            if column_index != -1 and is_valid_column(column_index, board):
                valid_move = True
                drop_checker(board, column_index, current_player)
            else:
                print("Invalid move. Please try again.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            game_over = True
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player_index = (current_player_index + 1) % NUM_PLAYERS

if __name__ == '__main__':
    main()