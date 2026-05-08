# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 108
# filename        : gen_0108_gemini_08.py
# timestamp       : 2026-04-06T09:54:26Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1386
# tokens_total    : 1762
# cost_usd        : 0.000592
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

# Constants
COLUMNS = 7
ROWS = 6
PLAYERS = 2
PLAYER_MARKS = ["X", "O"]

def create_board():
    """Creates an empty Connect 4 board."""
    board = []
    for _ in range(ROWS):
        row = [" "] * COLUMNS
        board.append(row)
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player_mark):
    """Gets a valid column choice from the player."""
    while True:
        column_choice = input(f"Player {player_mark}, choose a column (A-G): ").upper()

        if not column_choice.isalpha() or len(column_choice) != 1:
            print("Invalid input. Please enter a letter from A to G.")
            continue

        column_index = ord(column_choice) - ord('A')

        if column_index < 0 or column_index >= COLUMNS:
            print("Invalid column. Please choose a column between A and G.")
            continue

        if is_column_full(board, column_index):
            print("That column is full. Please choose another column.")
            continue

        return column_index

def is_column_full(board, column_index):
    """Checks if a column is full."""
    return board[0][column_index] != " "

def drop_checker(board, column_index, player_mark):
    """Drops the checker into the lowest available row in the chosen column."""
    for row_index in range(ROWS - 1, -1, -1):
        if board[row_index][column_index] == " ":
            board[row_index][column_index] = player_mark
            return row_index

def check_win(board, row_index, column_index, player_mark):
    """Checks for a win in all directions."""
    return (check_horizontal(board, row_index, column_index, player_mark) or
            check_vertical(board, row_index, column_index, player_mark) or
            check_diagonal_up(board, row_index, column_index, player_mark) or
            check_diagonal_down(board, row_index, column_index, player_mark))

def check_horizontal(board, row_index, column_index, player_mark):
    """Checks for a horizontal win."""
    count = 0
    for i in range(max(0, column_index - 3), min(COLUMNS, column_index + 4)):
        if board[row_index][i] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_vertical(board, row_index, column_index, player_mark):
    """Checks for a vertical win."""
    count = 0
    for i in range(max(0, row_index - 3), min(ROWS, row_index + 4)):
        if board[i][column_index] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_diagonal_up(board, row_index, column_index, player_mark):
    """Checks for a diagonal win (upwards)."""
    count = 0
    for i in range(-3, 4):
        r = row_index + i
        c = column_index + i
        if 0 <= r < ROWS and 0 <= c < COLUMNS:
            if board[r][c] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def check_diagonal_down(board, row_index, column_index, player_mark):
    """Checks for a diagonal win (downwards)."""
    count = 0
    for i in range(-3, 4):
        r = row_index - i
        c = column_index + i
        if 0 <= r < ROWS and 0 <= c < COLUMNS:
            if board[r][c] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)  # Randomly choose starting player

    print_board(board)

    while True:
        player_mark = PLAYER_MARKS[current_player]
        column_index = get_player_move(board, player_mark)
        row_index = drop_checker(board, column_index, player_mark)

        print_board(board)

        if check_win(board, row_index, column_index, player_mark):
            print(f"Player {player_mark} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```