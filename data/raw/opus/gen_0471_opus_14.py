# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 471
# filename        : gen_0471_opus_14.py
# timestamp       : 2026-05-07T22:45:22Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 416
# tokens_output   : 763
# tokens_total    : 1179
# cost_usd        : 0.063465
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
COLS=7
ROWS=6
PLAYERS=2
def make_board():
    return[[' 'for _ in range(COLS)]for _ in range(ROWS)]
def print_board(b):
    os.system('clear')
    print('   '+'   '.join([chr(65+i)for i in range(COLS)]))
    for r in range(ROWS):
        print('+---'*COLS+'+')
        print('|'+'|'.join([' '+b[r][c]+' 'for c in range(COLS)])+'|')
    print('+---'*COLS+'+')
def drop(b,col,p):
    for r in range(ROWS-1,-1,-1):
        if b[r][col]==' ':
            b[r][col]=p
            return r
    return-1
def check_win(b,p):
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(b[r][c+i]==p for i in range(4)):
                return True
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(b[r+i][c]==p for i in range(4)):
                return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(b[r+i][c+i]==p for i in range(4)):
                return True
    for r in range(3,ROWS):
        for c in range(COLS-3):
            if all(b[r-i][c+i]==p for i in range(4)):
                return True
    return False
def is_full(b):
    return all(b[0][c]!=' 'for c in range(COLS))
def get_move(b):
    while True:
        m=input("Enter column (A-G): ").strip()
        if len(m)!=1 or not m.isalpha():
            print("Invalid input. Enter a letter A-G.")
            continue
        m=m.upper()
        if m<'A'or m>'G':
            print("Invalid column. Enter A-G.")
            continue
        c=ord(m)-65
        if b[0][c]!=' ':
            print("Column full. Choose another.")
            continue
        return c
def main():
    b=make_board()
    players=['X','O']
    cur=random.randint(0,PLAYERS-1)
    print_board(b)
    while True:
        p=players[cur]
        print(f"Player {p}'s turn")
        c=get_move(b)
        drop(b,c,p)
        print_board(b)
        if check_win(b,p):
            print(f"{p} won!")
            break
        if is_full(b):
            print("Draw!")
            break
        cur=(cur+1)%PLAYERS
if __name__=="__main__":
    main()