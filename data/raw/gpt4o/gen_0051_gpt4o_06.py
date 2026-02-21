# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 51
# filename        : gen_0051_gpt4o_06.py
# timestamp       : 2026-02-19T20:47:08Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 572
# tokens_total    : 962
# cost_usd        : 0.006695
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

import os
import random

ROWS, COLS = 6, 7
PLAYERS = 2
COLUMN_LABELS = 'ABCDEFG'

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLS + '+')

def is_valid_input(choice):
    return choice in COLUMN_LABELS

def is_full_column(board, col):
    return board[0][col] != ' '

def make_move(board, col, checker):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = checker
            break

def check_winner(board, checker):
    for row in range(ROWS):
        for col in range(COLS):
            if (col <= COLS - 4 and all(board[row][col+i] == checker for i in range(4))) or \
               (row <= ROWS - 4 and all(board[row+i][col] == checker for i in range(4))) or \
               (col <= COLS - 4 and row <= ROWS - 4 and all(board[row+i][col+i] == checker for i in range(4))) or \
               (col >= 3 and row <= ROWS - 4 and all(board[row+i][col-i] == checker for i in range(4))):
                return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = create_board()
    print_board(board)
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        choice = input(f"Player {current_player}'s turn (A-G): ").strip()
        if not is_valid_input(choice):
            print("Invalid input. Choose a letter from A to G.")
            continue
        
        col = COLUMN_LABELS.index(choice)
        if is_full_column(board, col):
            print("Column is full. Choose another column.")
            continue
        
        make_move(board, col, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()