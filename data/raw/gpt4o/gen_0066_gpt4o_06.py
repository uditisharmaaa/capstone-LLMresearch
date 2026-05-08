# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 66
# filename        : gen_0066_gpt4o_06.py
# timestamp       : 2026-02-19T20:52:54Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 560
# tokens_total    : 950
# cost_usd        : 0.006575
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

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, PLAYER1, PLAYER2 = ' ', 'X', 'O'

def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join("A B C D E F G".split()))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def get_valid_column():
    while True:
        col = input("Choose a column (A-G): ").upper()
        if col in "ABCDEFG" and any(row["ABCDEFG".index(col)] == EMPTY for row in board):
            return "ABCDEFG".index(col)

def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = player
            break

def check_winner(board, player):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == player for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == player for i in range(4)):
                return True
    return False

def board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def main():
    board = create_board()
    players = [PLAYER1, PLAYER2]
    random.shuffle(players)
    current_player = 0
    print_board(board)

    while True:
        col = get_valid_column()
        make_move(board, col, players[current_player])
        print_board(board)
        
        if check_winner(board, players[current_player]):
            print(f"{players[current_player]} won!")
            break
        if board_full(board):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()
