# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 69
# filename        : gen_0069_gpt4o_09.py
# timestamp       : 2026-02-19T20:59:13Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 391
# tokens_output   : 631
# tokens_total    : 1022
# cost_usd        : 0.007288
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
COLUMN_LABELS = "ABCDEFG"

# Initialize board
def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+" + "---+" * COLUMNS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * COLUMNS)

def get_column_input():
    while True:
        col = input("Choose a column (A-G): ").strip().upper()
        if col in COLUMN_LABELS:
            return COLUMN_LABELS.index(col)
        print("Invalid input. Please enter a letter between A-G.")

def is_valid_move(board, col):
    return board[0][col] == ' '

def make_move(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row

def check_winner(board, row, col, checker):
    # Horizontal, Vertical, Diagonal checks
    def check_line(delta_row, delta_col):
        count = 0
        for d in range(-3, 4):
            r, c = row + d * delta_row, col + d * delta_col
            if 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == checker:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    
    return (check_line(0, 1) or  # Horizontal
            check_line(1, 0) or  # Vertical
            check_line(1, 1) or  # Diagonal /
            check_line(1, -1))   # Diagonal \

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def play_game():
    board = create_board()
    current_player = random.choice(['X', 'O'])
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn")
        col = get_column_input()
        
        if is_valid_move(board, col):
            row = make_move(board, col, current_player)
            print_board(board)
            
            if check_winner(board, row, col, current_player):
                print(f"Player {current_player} won!")
                break
            elif is_draw(board):
                print("The game is a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Column is full. Try a different column.")

if __name__ == "__main__":
    play_game()