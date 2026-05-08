# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 113
# filename        : gen_0113_gemini_13.py
# timestamp       : 2026-04-06T09:55:31Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1222
# tokens_total    : 1596
# cost_usd        : 0.000526
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
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_MARKS = ["X", "O"]


def clear_screen():
    os.system('clear')


def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board


def print_board(board):
    """Prints the Connect 4 board with column labels."""
    print("  ", end="")
    for i in range(BOARD_WIDTH):
        print(chr(ord('A') + i), end="   ")
    print()

    for row in range(BOARD_HEIGHT):
        print("+", end="")
        for _ in range(BOARD_WIDTH):
            print("---+", end="")
        print()
        print("|", end="")
        for col in range(BOARD_WIDTH):
            print(" " + board[row][col] + " |", end="")
        print()

    print("+", end="")
    for _ in range(BOARD_WIDTH):
        print("---+", end="")
    print()


def get_player_move(board, player_mark):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player_mark}, enter column (A-G): ").upper()

        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column_index = ord(column_input) - ord('A')

        if not (0 <= column_index < BOARD_WIDTH):
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][column_index] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column_index


def drop_checker(board, column_index, player_mark):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column_index] == " ":
            board[row][column_index] = player_mark
            return row


def check_win(board, row, col, player_mark):
    """Checks for a win horizontally, vertically, and diagonally."""

    # Horizontal
    count = 0
    for c in range(max(0, col - 3), min(BOARD_WIDTH, col + 4)):
        if board[row][c] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for r in range(max(0, row - 3), min(BOARD_HEIGHT, row + 4)):
        if board[r][col] == player_mark:
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
            if board[r][c] == player_mark:
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
            if board[r][c] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False


def check_draw(board):
    """Checks if the board is full."""
    for col in range(BOARD_WIDTH):
        if board[0][col] == " ":
            return False
    return True


def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player_turn = random.randint(0, NUM_PLAYERS - 1)  # Randomly select first player

    clear_screen()
    print_board(board)

    while True:
        player_mark = PLAYER_MARKS[player_turn]
        column_index = get_player_move(board, player_mark)
        row = drop_checker(board, column_index, player_mark)

        clear_screen()
        print_board(board)

        if check_win(board, row, column_index, player_mark):
            print(f"Player {player_mark} won!")
            break

        if check_draw(board):
            print("Draw!")
            break

        player_turn = (player_turn + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()
```