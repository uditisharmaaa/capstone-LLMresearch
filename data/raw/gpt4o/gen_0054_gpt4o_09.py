# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 54
# filename        : gen_0054_gpt4o_09.py
# timestamp       : 2026-02-19T20:47:41Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 391
# tokens_output   : 729
# tokens_total    : 1120
# cost_usd        : 0.008268
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
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLUMNS + '+')

def is_valid_move(board, column):
    return 0 <= column < COLUMNS and board[0][column] == ' '

def get_next_open_row(board, column):
    for r in range(ROWS-1, -1, -1):
        if board[r][column] == ' ':
            return r

def make_move(board, row, column, piece):
    board[row][column] = piece

def check_win(board, piece):
    # Check horizontal
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    
    # Check vertical
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLUMNS))

def get_player_input(player):
    while True:
        try:
            choice = input(f"Player {player}, choose a column (A-G): ").strip().upper()
            if choice in COLUMN_LABELS:
                return COLUMN_LABELS.index(choice)
            else:
                print("Invalid input. Please choose a column between A and G.")
        except ValueError:
            print("Invalid input. Please enter a valid column letter.")

def main():
    board = create_board()
    game_over = False
    turn = random.randint(0, PLAYERS - 1)
    pieces = ['X', 'O']

    while not game_over:
        print_board(board)
        player = turn % PLAYERS + 1
        column = get_player_input(player)
        
        if is_valid_move(board, column):
            row = get_next_open_row(board, column)
            make_move(board, row, column, pieces[turn % PLAYERS])

            if check_win(board, pieces[turn % PLAYERS]):
                print_board(board)
                print(f"Player {player} won!")
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("The game is a draw!")
                game_over = True
            else:
                turn += 1

main()