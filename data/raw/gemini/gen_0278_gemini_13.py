# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 278
# filename        : gen_0278_gemini_13.py
# timestamp       : 2026-04-06T10:28:41Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1123
# tokens_total    : 1497
# cost_usd        : 0.000487
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_CHARS = ["X", "O"]

def create_board():
    """Creates a 2D board with ROWS and COLS, initialized with spaces."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(COLS):
            print(f" {board[row][col]} |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid column choice from the player."""
    while True:
        column_choice = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not column_choice.isalpha() or len(column_choice) != 1:
            print("Invalid input. Please enter a single letter (A-G).")
            continue

        column_index = ord(column_choice) - ord('A')
        if not (0 <= column_index < COLS):
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][column_index] != " ":
            print("Column is full. Please choose a different column.")
            continue

        return column_index

def drop_checker(board, column, player_char):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player_char
            return row

def check_win(board, row, col, player_char):
    """Checks for a win in horizontal, vertical, and diagonal directions."""

    # Horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)  # Randomly choose the first player
    game_over = False

    print_board(board)

    while not game_over:
        column = get_player_move(board, current_player)
        row = drop_checker(board, column, PLAYER_CHARS[current_player])
        print_board(board)

        if check_win(board, row, column, PLAYER_CHARS[current_player]):
            print(f"Player {current_player + 1} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```