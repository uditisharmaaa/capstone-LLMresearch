# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 274
# filename        : gen_0274_gemini_09.py
# timestamp       : 2026-04-06T10:28:22Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 380
# tokens_output   : 925
# tokens_total    : 1305
# cost_usd        : 0.000408
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

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for i in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for j in range(COLS):
            row_str += " " + board[i][j] + " |"
        print(row_str)
    print("+---+---+---+---+---+---+---+")

def get_player_move(player, board):
    while True:
        move = input(f"Player {player}, enter column (A-G): ").upper()
        if len(move) != 1 or move not in "ABCDEFG":
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = ord(move) - ord('A')
        if board[0][col] != " ":
            print("Column is full. Choose another column.")
            continue
        return col

def drop_checker(board, col, player):
    for i in range(ROWS - 1, -1, -1):
        if board[i][col] == " ":
            board[i][col] = player
            return i

def check_win(board, row, col, player):
    # Check horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for i in range(ROWS):
        if board[i][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = create_board()
    player1 = PLAYER_X
    player2 = PLAYER_O
    current_player = random.choice([player1, player2])
    print_board(board)

    while True:
        col = get_player_move(current_player, board)
        row = drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, row, col, current_player):
            print(f"{current_player} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```