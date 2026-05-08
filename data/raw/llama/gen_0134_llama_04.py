# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 134
# filename        : gen_0134_llama_04.py
# timestamp       : 2026-04-06T10:00:31Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 394
# tokens_output   : 799
# tokens_total    : 1193
# cost_usd        : 0.000804
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

```python
import os
import random

# Constant global variables
BOARD_COLUMNS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

def print_board(board):
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| {} |".format(" | ".join(row)))
        print("+---+---+---+---+---+---+---+")

def is_valid_move(board, column):
    return board[0][column] == " "

def get_player_move(board, player):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player))
        if len(move)!= 1 or not move.isalpha():
            print("Invalid input. Please enter a single letter (A-G).")
            continue
        column = ord(move.upper()) - ord('A')
        if column < 0 or column >= BOARD_COLUMNS:
            print("Invalid column. Please choose a column between A and G.")
            continue
        if not is_valid_move(board, column):
            print("Column is full. Please choose another column.")
            continue
        return column

def drop_checker(board, column, player):
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            break

def check_win(board, player):
    # Check horizontal locations for win
    for c in range(BOARD_COLUMNS - 3):
        for r in range(BOARD_ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(BOARD_COLUMNS):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_COLUMNS - 3):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_COLUMNS - 3):
        for r in range(3, BOARD_ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

def main():
    board = [[" " for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]
    players = ["X", "O"]
    current_player = random.choice(players)
    print_board(board)

    while True:
        column = get_player_move(board, current_player)
        drop_checker(board, column, current_player)
        print_board(board)
        if check_win(board, current_player):
            print("Player {} won!".format(current_player))
            break
        current_player = "O" if current_player == "X" else "X"
        if all([all([cell!= " " for cell in row]) for row in board]):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
```