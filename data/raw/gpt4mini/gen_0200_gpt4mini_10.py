# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 200
# filename        : gen_0200_gpt4mini_10.py
# timestamp       : 2026-04-06T09:28:02Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 390
# tokens_output   : 701
# tokens_total    : 1091
# cost_usd        : 0.000479
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_CHECKERS = ['X', 'O']

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def get_column_input():
    while True:
        col_input = input("Choose a column (A-G): ").upper()
        if col_input in 'ABCDEFG':
            return ord(col_input) - ord('A')
        print("Invalid input. Please choose a letter between A and G.")

def is_column_full(board, col):
    return board[0][col] != ' '

def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row
    return -1

def check_winner(board, checker):
    # Check horizontal, vertical, and diagonal wins
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == checker:
                if check_direction(board, r, c, 0, 1, checker) or \
                   check_direction(board, r, c, 1, 0, checker) or \
                   check_direction(board, r, c, 1, 1, checker) or \
                   check_direction(board, r, c, 1, -1, checker):
                    return True
    return False

def check_direction(board, r, c, dr, dc, checker):
    count = 0
    for i in range(4):
        rr = r + dr * i
        cc = c + dc * i
        if 0 <= rr < ROWS and 0 <= cc < COLS and board[rr][cc] == checker:
            count += 1
        else:
            break
    return count == 4

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    
    while True:
        print_board(board)
        checker = PLAYER_CHECKERS[current_player]
        
        while True:
            col = get_column_input()
            if not is_column_full(board, col):
                break
            print("Column is full. Choose another column.")
        
        drop_checker(board, col, checker)
        
        if check_winner(board, checker):
            print_board(board)
            print(f"{checker} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()