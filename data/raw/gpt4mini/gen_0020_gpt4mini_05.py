# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 20
# filename        : gen_0020_gpt4mini_05.py
# timestamp       : 2026-02-19T20:35:53Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 655
# tokens_total    : 1042
# cost_usd        : 0.000451
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

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ["X", "O"]

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(column):
    return column in 'ABCDEFG'

def get_column_choice(player):
    while True:
        column = input(f"Player {PLAYER_SYMBOLS[player]}, choose a column (A-G): ").upper()
        if is_valid_input(column):
            col_index = ord(column) - ord('A')
            if board[0][col_index] == ' ':
                return col_index
            else:
                print("Column is full! Try again.")
        else:
            print("Invalid input! Please choose a column between A and G.")

def drop_checker(board, column, player):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = PLAYER_SYMBOLS[player]
            return True
    return False

def check_winner(board, player):
    symbol = PLAYER_SYMBOLS[player]
    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == symbol:
                if check_direction(board, r, c, 1, 0) or check_direction(board, r, c, 0, 1) or check_direction(board, r, c, 1, 1) or check_direction(board, r, c, 1, -1):
                    return True
    return False

def check_direction(board, r, c, dr, dc):
    count = 0
    for i in range(4):
        rr = r + dr * i
        cc = c + dc * i
        if 0 <= rr < ROWS and 0 <= cc < COLS and board[rr][cc] == board[r][c]:
            count += 1
        else:
            break
    return count == 4

def is_draw(board):
    return all(board[0][c] != ' ' for c in range(COLS))

def play_game():
    board = create_board()
    current_player = random.randint(0, 1)
    
    while True:
        print_board(board)
        column = get_column_choice(current_player)
        drop_checker(board, column, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    play_game()