# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 138
# filename        : gen_0138_gemini_08.py
# timestamp       : 2026-04-06T10:02:54Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1064
# tokens_total    : 1440
# cost_usd        : 0.000463
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
#   Write with a focus on code readability over brevity.
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
    """Creates a 2D board with spaces."""
    board = []
    for _ in range(ROWS):
        row = [" "] * COLS
        board.append(row)
    return board

def print_board(board):
    """Prints the board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        column_letter = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_letter.isalpha() or len(column_letter) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        try:
            column = ord(column_letter) - ord('A')
            if not 0 <= column < COLS:
                print("Invalid column. Please choose a column between A and G.")
                continue
            if board[0][column] != " ":
                print("Column is full. Please choose a different column.")
                continue
            return column
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def drop_checker(board, column, player):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return row

def check_win(board, row, col, player):
    """Checks for a win in all directions."""
    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player:
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
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1 = PLAYER_X
    player2 = PLAYER_O

    # Randomly select which player goes first
    current_player = random.choice([player1, player2])

    print_board(board)

    while True:
        column = get_player_move(board, current_player)
        row = drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, row, column, current_player):
            print(f"{current_player} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```