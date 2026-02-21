# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 92
# filename        : gen_0092_gpt4o_02.py
# timestamp       : 2026-02-19T21:03:45Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 595
# tokens_total    : 984
# cost_usd        : 0.006922
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, PLAYER1, PLAYER2 = ' ', 'X', 'O'
COLUMN_LABELS = 'ABCDEFG'

def clear_screen():
    os.system('clear')

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLS + '+')

def get_move():
    while True:
        move = input("Choose a column (A-G): ").strip()
        if len(move) == 1 and move in COLUMN_LABELS:
            return COLUMN_LABELS.index(move)

def is_valid_move(board, col):
    return board[0][col] == EMPTY

def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = player
            break

def check_line(line):
    count = 0
    last = EMPTY
    for cell in line:
        if cell == last and cell != EMPTY:
            count += 1
            if count == 4:
                return True
        else:
            count = 1
            last = cell
    return False

def check_win(board, player):
    for row in board:
        if check_line(row):
            return True
    for col in range(COLS):
        if check_line([board[row][col] for row in range(ROWS)]):
            return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if check_line([board[r+i][c+i] for i in range(4)]) or check_line([board[r+3-i][c+i] for i in range(4)]):
                return True
    return False

def board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def connect4():
    board = create_board()
    players = [PLAYER1, PLAYER2]
    current_player = random.choice(players)
    print_board(board)
    while True:
        print(f"Player {current_player}'s turn.")
        col = get_move()
        if is_valid_move(board, col):
            make_move(board, col, current_player)
            print_board(board)
            if check_win(board, current_player):
                print(f"Player {current_player} won!")
                break
            if board_full(board):
                print("It's a draw!")
                break
            current_player = PLAYER1 if current_player == PLAYER2 else PLAYER2

connect4()