# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 95
# filename        : gen_0095_gpt4o_05.py
# timestamp       : 2026-02-19T21:04:23Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 612
# tokens_total    : 999
# cost_usd        : 0.007088
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

# Constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_player_input(board, player):
    while True:
        move = input(f"Player {player} ({PLAYER_SYMBOLS[player]}), choose a column (A-G): ").strip()
        if len(move) == 1 and move in COLUMN_LABELS:
            column = COLUMN_LABELS.index(move)
            if board[0][column] == ' ':
                return column
            else:
                print("Column is full. Try another one.")
        else:
            print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, column, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = PLAYER_SYMBOLS[player]
            return row

def check_winner(board, row, column, player):
    def count_consecutive(r_step, c_step):
        r, c = row, column
        count = 0
        while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == PLAYER_SYMBOLS[player]:
            count += 1
            r += r_step
            c += c_step
        return count

    direction_vectors = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in direction_vectors:
        if count_consecutive(dr, dc) + count_consecutive(-dr, -dc) - 1 >= 4:
            return True
    return False

def is_draw(board):
    return all(cell != ' ' for cell in board[0])

def connect_four():
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS-1)
    print_board(board)

    while True:
        column = get_player_input(board, current_player)
        row = drop_checker(board, column, current_player)
        print_board(board)

        if check_winner(board, row, column, current_player):
            print(f"Player {current_player} ({PLAYER_SYMBOLS[current_player]}) won!")
            break

        if is_draw(board):
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS

connect_four()