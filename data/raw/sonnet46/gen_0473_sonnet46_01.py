# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 473
# filename        : gen_0473_sonnet46_01.py
# timestamp       : 2026-05-07T22:45:52Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1277
# tokens_total    : 1698
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(NUM_ROWS):
        board.append([' '] * NUM_COLS)
    return board

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    for row in range(NUM_ROWS):
        print('+---+---+---+---+---+---+---+')
        row_string = '|'
        for col in range(NUM_COLS):
            row_string += ' ' + board[row][col] + ' |'
        print(row_string)
    print('+---+---+---+---+---+---+---+')

def get_player_input(board, player_checker):
    column_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    while True:
        player_input = input('Player ' + player_checker + ', choose a column (A-G): ')
        if len(player_input) == 0:
            print('Invalid input. Please enter a letter between A and G.')
            continue
        letter = player_input[0].upper()
        if letter not in column_letters:
            print('Invalid input. Please enter a letter between A and G.')
            continue
        chosen_col = column_letters.index(letter)
        if board[0][chosen_col] != ' ':
            print('That column is full. Please choose another column.')
            continue
        return chosen_col

def drop_checker(board, col, player_checker):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player_checker
            return row
    return -1

def check_horizontal_win(board, player_checker):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player_checker and
                    board[row][col + 1] == player_checker and
                    board[row][col + 2] == player_checker and
                    board[row][col + 3] == player_checker):
                return True
    return False

def check_vertical_win(board, player_checker):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if (board[row][col] == player_checker and
                    board[row + 1][col] == player_checker and
                    board[row + 2][col] == player_checker and
                    board[row + 3][col] == player_checker):
                return True
    return False

def check_diagonal_win(board, player_checker):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player_checker and
                    board[row + 1][col + 1] == player_checker and
                    board[row + 2][col + 2] == player_checker and
                    board[row + 3][col + 3] == player_checker):
                return True
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player_checker and
                    board[row - 1][col + 1] == player_checker and
                    board[row - 2][col + 2] == player_checker and
                    board[row - 3][col + 3] == player_checker):
                return True
    return False

def check_win(board, player_checker):
    if check_horizontal_win(board, player_checker):
        return True
    if check_vertical_win(board, player_checker):
        return True
    if check_diagonal_win(board, player_checker):
        return True
    return False

def check_draw(board):
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            return False
    return True

def play_game():
    board = create_board()
    checkers = ['X', 'O']
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    game_over = False

    print_board(board)

    while not game_over:
        current_checker = checkers[current_player_index]
        chosen_col = get_player_input(board, current_checker)
        drop_checker(board, chosen_col, current_checker)
        print_board(board)

        if check_win(board, current_checker):
            print('Player ' + current_checker + ' won!')
            game_over = True
        elif check_draw(board):
            print('The game is a draw!')
            game_over = True
        else:
            current_player_index = (current_player_index + 1) % NUM_PLAYERS

play_game()