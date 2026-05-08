# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 246
# filename        : gen_0246_gemini_11.py
# timestamp       : 2026-04-06T10:24:59Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 375
# tokens_output   : 1110
# tokens_total    : 1485
# cost_usd        : 0.000482
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
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_TOKENS = ["X", "O"]


def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board


def print_board(board):
    """Prints the Connect 4 board to the console."""
    os.system('clear')
    print("  " + "   ".join(chr(ord('A') + i) for i in range(BOARD_WIDTH)))
    for row in board:
        print("+---" * BOARD_WIDTH + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * BOARD_WIDTH + "+")


def get_player_move(board, player_token):
    """Gets a valid move from the current player."""
    while True:
        column_input = input(f"Player {player_token}, enter column (A-G): ").upper()

        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column_index = ord(column_input) - ord('A')

        if not 0 <= column_index < BOARD_WIDTH:
            print("Invalid column. Please enter a letter A-G.")
            continue

        if board[0][column_index] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column_index


def drop_checker(board, column_index, player_token):
    """Drops the player's checker into the specified column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column_index] == " ":
            board[row][column_index] = player_token
            return row


def check_win(board, row, col, player_token):
    """Checks if the current move resulted in a win."""
    # Check horizontal
    count = 0
    for c in range(BOARD_WIDTH):
        if board[row][c] == player_token:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(BOARD_HEIGHT):
        if board[r][col] == player_token:
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
            if board[r][c] == player_token:
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
            if board[r][c] == player_token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False


def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for row in board:
        if " " in row:
            return False
    return True


def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    player_tokens = PLAYER_TOKENS
    print_board(board)

    while True:
        player_token = player_tokens[current_player]
        column_index = get_player_move(board, player_token)
        row_index = drop_checker(board, column_index, player_token)
        print_board(board)

        if check_win(board, row_index, column_index, player_token):
            print(f"Player {player_token} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()
```