# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 399
# filename        : gen_0399_sonnet46_09.py
# timestamp       : 2026-05-07T19:11:17Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 420
# tokens_output   : 1052
# tokens_total    : 1472
# cost_usd        : 0.000000
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

NUM_COLS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(NUM_ROWS):
        board.append([])
        for col in range(NUM_COLS):
            board[row].append(' ')
    return board

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    for row in range(NUM_ROWS):
        print('+---+---+---+---+---+---+---+')
        line = '|'
        for col in range(NUM_COLS):
            line = line + ' ' + board[row][col] + ' ' + '|'
        print(line)
    print('+---+---+---+---+---+---+---+')

def get_player_input(board, player):
    valid_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    while True:
        choice = input('Player ' + player + ', choose a column (A-G): ')
        if len(choice) == 0:
            print('Invalid input. Please enter a letter A through G.')
            continue
        choice = choice[0].upper()
        if choice not in valid_columns:
            print('Invalid input. Please enter a letter A through G.')
            continue
        col_index = ord(choice) - ord('A')
        if board[0][col_index] != ' ':
            print('That column is full. Please choose another column.')
            continue
        return col_index

def drop_checker(board, col_index, checker):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_index] == ' ':
            board[row][col_index] = checker
            return row
    return -1

def check_win(board, checker):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == checker and board[row][col+1] == checker and board[row][col+2] == checker and board[row][col+3] == checker:
                return True

    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if board[row][col] == checker and board[row+1][col] == checker and board[row+2][col] == checker and board[row+3][col] == checker:
                return True

    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if board[row][col] == checker and board[row+1][col+1] == checker and board[row+2][col+2] == checker and board[row+3][col+3] == checker:
                return True

    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == checker and board[row-1][col+1] == checker and board[row-2][col+2] == checker and board[row-3][col+3] == checker:
                return True

    return False

def check_draw(board):
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            return False
    return True

def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player_index = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        current_player = players[current_player_index]
        col_index = get_player_input(board, current_player)
        drop_checker(board, col_index, current_player)
        print_board(board)

        if check_win(board, current_player):
            print('Player ' + current_player + ' won!')
            break

        if check_draw(board):
            print('It is a draw!')
            break

        current_player_index = (current_player_index + 1) % NUM_PLAYERS

play_game()