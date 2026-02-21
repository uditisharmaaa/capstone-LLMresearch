# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 62
# filename        : gen_0062_gpt4o_02.py
# timestamp       : 2026-02-19T20:51:56Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 513
# tokens_total    : 902
# cost_usd        : 0.006103
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

import os,random

ROWS,COLS,PLAYERS=6,7,2
board=[[' ']*COLS for _ in range(ROWS)]
current_player=random.choice(['X','O'])

def clear_screen():
    os.system('clear')

def print_board():
    clear_screen()
    print("   " + "   ".join("ABCDEFG"))
    for row in board:
        print("+---"*COLS+"+")
        print("| " + " | ".join(row) + " |")
    print("+---"*COLS+"+")

def is_valid_move(col):
    return col in range(COLS) and board[0][col] == ' '

def make_move(col,player):
    for row in range(ROWS-1,-1,-1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row

def check_win(row,col):
    def check_dir(delta_row,delta_col):
        count,p,r,c=1,board[row][col],row+delta_row,col+delta_col
        while 0<=r<ROWS and 0<=c<COLS and board[r][c]==p:
            count+=1
            r+=delta_row
            c+=delta_col
        return count
    directions=[(1,0),(0,1),(1,1),(1,-1)]
    for dr,dc in directions:
        if check_dir(dr,dc)+check_dir(-dr,-dc)-1 >= 4:
            return True
    return False

def is_draw():
    return all(board[0][c] != ' ' for c in range(COLS))

def get_col_from_input():
    while True:
        try:
            col=input(f"Player {current_player}, choose a column (A-G): ").strip().upper()
            if col in "ABCDEFG" and is_valid_move(ord(col)-ord('A')):
                return ord(col)-ord('A')
        except:
            pass
        print("Invalid input. Please try again.")

def play_game():
    global current_player
    print_board()
    while True:
        col=get_col_from_input()
        row=make_move(col,current_player)
        print_board()
        if check_win(row,col):
            print(f"Player {current_player} won!")
            break
        if is_draw():
            print("It's a draw!")
            break
        current_player='O' if current_player=='X' else 'X'

play_game()