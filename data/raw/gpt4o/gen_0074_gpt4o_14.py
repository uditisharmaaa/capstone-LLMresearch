# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 74
# filename        : gen_0074_gpt4o_14.py
# timestamp       : 2026-02-19T21:00:03Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 699
# tokens_total    : 1086
# cost_usd        : 0.007957
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

import os
import random

ROWS=6
COLS=7
PLAYERS=2

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ']*COLS for _ in range(ROWS)]

def print_board(b):
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---"*COLS+"+")
    for r in b:
        print("|"+"|".join(f" {c} " for c in r)+"|")
        print("+---"*COLS+"+")

def is_valid_move(b,col):
    return b[0][col]==' '

def get_next_open_row(b,col):
    for r in range(ROWS-1,-1,-1):
        if b[r][col]==' ':
            return r

def drop_checker(b,row,col,piece):
    b[row][col]=piece

def winning_move(b,piece):
    for c in range(COLS-3):
        for r in range(ROWS):
            if b[r][c]==piece and b[r][c+1]==piece and b[r][c+2]==piece and b[r][c+3]==piece:
                return True
    for c in range(COLS):
        for r in range(ROWS-3):
            if b[r][c]==piece and b[r+1][c]==piece and b[r+2][c]==piece and b[r+3][c]==piece:
                return True
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if b[r][c]==piece and b[r+1][c+1]==piece and b[r+2][c+2]==piece and b[r+3][c+3]==piece:
                return True
    for c in range(COLS-3):
        for r in range(3,ROWS):
            if b[r][c]==piece and b[r-1][c+1]==piece and b[r-2][c+2]==piece and b[r-3][c+3]==piece:
                return True

def full_board(b):
    return all(b[0][c]!=' ' for c in range(COLS))

def main():
    board=create_board()
    game_over=False
    turn=random.randint(0,PLAYERS-1)
    pieces=['X','O']

    while not game_over:
        print_board(board)
        col=None
        while col is None:
            move=input(f"Player {pieces[turn % PLAYERS]}, make your move (A-G): ").strip().upper()
            if move in "ABCDEFG":
                col=ord(move)-ord('A')
                if not is_valid_move(board,col):
                    print("Column full, try again.")
                    col=None
            else:
                print("Invalid input, try again.")

        row=get_next_open_row(board,col)
        drop_checker(board,row,col,pieces[turn%PLAYERS])

        if winning_move(board,pieces[turn%PLAYERS]):
            print_board(board)
            print(f"Player {pieces[turn%PLAYERS]} won!")
            game_over=True
        elif full_board(board):
            print_board(board)
            print("It's a draw!")
            game_over=True
        else:
            turn+=1

if __name__=="__main__":
    main()