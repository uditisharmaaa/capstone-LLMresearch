# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 261
# filename        : gen_0261_gemini_11.py
# timestamp       : 2026-04-06T10:27:12Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 375
# tokens_output   : 1137
# tokens_total    : 1512
# cost_usd        : 0.000492
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
#   Write with extensive docstrings for every function.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_CHECKERS = ["X", "O"]


def create_board():
    """Creates a 2D board for Connect 4, initialized with spaces."""
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board


def print_board(board):
    """Prints the Connect 4 board with column labels and formatting."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for i in range(ROWS):
        print("+---" * COLS + "+")
        print("|", end=" ")
        for j in range(COLS):
            print(board[i][j], end=" | ")
        print()
    print("+---" * COLS + "+")


def get_player_move(player_num, board):
    """
    Gets a valid column choice from the player.
    Keeps prompting until a valid input is given.
    """
    while True:
        column_str = input(f"Player {player_num + 1}, enter column (A-G): ").upper()
        if not column_str.isalpha() or len(column_str) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(column_str) - ord('A')

        if 0 <= column < COLS:
            if board[0][column] == ' ':
                return column
            else:
                print("That column is full. Try again.")
        else:
            print("Invalid column. Please enter a letter A-G.")


def drop_checker(board, column, checker):
    """Drops the checker into the lowest available row in the chosen column."""
    for i in range(ROWS - 1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = checker
            return i, column  # Return the row and column where the checker was placed
    return None


def check_win(board, row, col, checker):
    """Checks if the last move resulted in a win (4 in a row)."""

    # Check horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for i in range(ROWS):
        if board[i][col] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r, c = row - i, col - i
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r, c = row - i, col + i
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for row in board:
        if ' ' in row:
            return False  # Found an empty space, not a draw
    return True  # No empty spaces, it's a draw


def play_game():
    """Main function to play the Connect 4 game."""
    board = create_board()
    player_turn = random.randint(0, PLAYERS - 1)  # Randomly choose starting player
    print_board(board)

    while True:
        column = get_player_move(player_turn, board)
        row, col = drop_checker(board, column, PLAYER_CHECKERS[player_turn])

        print_board(board)

        if check_win(board, row, col, PLAYER_CHECKERS[player_turn]):
            print(f"Player {player_turn + 1} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        player_turn = (player_turn + 1) % PLAYERS  # Switch to the next player


if __name__ == "__main__":
    play_game()
```