# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 89
# filename        : gen_0089_gpt4o_14.py
# timestamp       : 2026-02-19T21:03:09Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 468
# tokens_total    : 855
# cost_usd        : 0.005647
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

import os,random

ROWS,COLS,PLAYERS=6,7,2
BOARD=[[' 'for _ in range(COLS)]for _ in range(ROWS)]
CHARS='ABCDEFG'
CHECKERS=['X','O']

def clear_screen():os.system('clear')

def print_board():
    clear_screen()
    print('   '.join(CHARS))
    print('+---'*COLS+'+')
    for r in BOARD:
        print('|'+'|'.join(r)+'|')
        print('+---'*COLS+'+')

def is_valid_move(col):
    return col in CHARS and BOARD[0][CHARS.index(col)]==' '

def make_move(col,checker):
    c=CHARS.index(col)
    for r in range(ROWS-1,-1,-1):
        if BOARD[r][c]==' ':
            BOARD[r][c]=checker
            return r,c

def check_win(r,c,checker):
    def count(dx,dy):
        x,y=c,r
        cnt=0
        for _ in range(3):
            x+=dx
            y+=dy
            if 0<=x<COLS and 0<=y<ROWS and BOARD[y][x]==checker:
                cnt+=1
            else:
                break
        return cnt
    return any(count(dx,dy)+count(-dx,-dy)>=3 for dx,dy in [(1,0),(0,1),(1,1),(1,-1)])

def is_draw():
    return all(BOARD[0][c]!=' 'for c in range(COLS))

def main():
    player=random.choice([0,1])
    print_board()
    while True:
        col=input(f"Player {CHECKERS[player]}'s turn (A-G): ").strip().upper()
        if is_valid_move(col):
            r,c=make_move(col,CHECKERS[player])
            print_board()
            if check_win(r,c,CHECKERS[player]):
                print(f"Player {CHECKERS[player]} won!")
                break
            if is_draw():
                print("It's a draw!")
                break
            player=(player+1)%PLAYERS
        else:
            print("Invalid move. Try again.")

if __name__=='__main__':
    main()