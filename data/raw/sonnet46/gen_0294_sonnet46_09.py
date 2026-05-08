# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 294
# filename        : gen_0294_sonnet46_09.py
# timestamp       : 2026-05-07T17:02:03Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 420
# tokens_output   : 931
# tokens_total    : 1351
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
        line = ''
        for col in range(NUM_COLS):
            line = line + '| ' + board[row][col] + ' '
        line = line + '|'
        print(line)
    print('+---+---+---+---+---+---+---+')

def get_player_move(board, player):
    while True:
        move = input('Player ' + player + ', choose a column (A-G): ')
        if len(move) != 1:
            print('Invalid input. Please enter a single letter from A to G.')
            continue
        if not move.isalpha():
            print('Invalid input. Please enter a letter from A to G.')
            continue
        move = move.upper()
        if move < 'A' or move > 'G':
            print('Invalid input. Please enter a letter from A to G.')
            continue
        col = ord(move) - ord('A')
        if board[0][col] != ' ':
            print('That column is full. Please choose another column.')
            continue
        return col

def drop_checker(board, col, player):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row
    return -1

def check_win(board, row, col, player):
    directions = []
    directions.append((0, 1))
    directions.append((1, 0))
    directions.append((1, 1))
    directions.append((1, -1))

    for dr, dc in directions:
        count = 1

        r = row + dr
        c = col + dc
        while r >= 0 and r < NUM_ROWS and c >= 0 and c < NUM_COLS and board[r][c] == player:
            count = count + 1
            r = r + dr
            c = c + dc

        r = row - dr
        c = col - dc
        while r >= 0 and r < NUM_ROWS and c >= 0 and c < NUM_COLS and board[r][c] == player:
            count = count + 1
            r = r - dr
            c = c - dc

        if count >= 4:
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
    current = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        player = players[current]
        col = get_player_move(board, player)
        row = drop_checker(board, col, player)
        print_board(board)

        if check_win(board, row, col, player):
            print('Player ' + player + ' won!')
            break

        if check_draw(board):
            print('The game is a draw!')
            break

        current = (current + 1) % NUM_PLAYERS

play_game()