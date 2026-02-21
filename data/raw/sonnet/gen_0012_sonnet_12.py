# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 12
# filename        : gen_0012_sonnet_12.py
# timestamp       : 2026-02-19T20:34:02Z
# model           : anthropic/claude-3.5-sonnet
# model_short     : sonnet
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 418
# tokens_output   : 822
# tokens_total    : 1240
# cost_usd        : 0.013584
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
PLAYERS = ['X', 'O']
WIN_LENGTH = 4

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('|', end=' ')
        print(' | '.join(row), end=' ')
        print('|')
    print('+---+---+---+---+---+---+---+')

def get_column_choice():
    while True:
        try:
            choice = input("Choose a column (A-G): ").upper()
            if len(choice) != 1 or not 'A' <= choice <= 'G':
                raise ValueError
            return ord(choice) - ord('A')
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def is_valid_move(board, col):
    return board[0][col] == ' '

def drop_checker(board, col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row

def check_win(board, row, col, player):
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    
    for dr, dc in directions:
        count = 1
        # Check forward
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        
        # Check backward
        r, c = row - dr, col - dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
            
        if count >= WIN_LENGTH:
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = create_board()
    current_player = random.choice(PLAYERS)
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            col = get_column_choice()
            if is_valid_move(board, col):
                break
            print("That column is full. Try again.")
        
        row = drop_checker(board, col, current_player)
        
        if check_win(board, row, col, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()