# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 118
# filename        : gen_0118_gemini_03.py
# timestamp       : 2026-04-06T09:56:28Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1182
# tokens_total    : 1557
# cost_usd        : 0.000510
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

```python
import os
import random

# Define global constants for board dimensions and players
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_MARKS = ["X", "O"]

def create_board():
    """Creates a 2D board represented as a list of lists, initialized with spaces."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the board with column labels."""
    os.system('clear')  # Clear the screen

    # Print column labels
    print("  " + "   ".join([chr(65 + i) for i in range(COLS)]))  # A, B, C, D, E, F, G

    # Print the board with separators
    for row in board:
        print("+---" * COLS + "+")  # Top border
        print("| " + " | ".join(row) + " |")  # Cell content
    print("+---" * COLS + "+")  # Bottom border

def get_player_move(board, player_mark):
    """Gets a valid move from the player."""
    while True:
        try:
            column_letter = input(f"Player {player_mark}, choose a column (A-G): ").upper()
            column_index = ord(column_letter) - ord('A')

            # Validate input
            if not (0 <= column_index < COLS):
                print("Invalid column. Choose a letter between A and G.")
                continue

            if board[0][column_index] != " ":
                print("That column is full. Choose another column.")
                continue

            return column_index

        except (ValueError, TypeError):
            print("Invalid input. Please enter a letter (A-G).")

def drop_checker(board, column_index, player_mark):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column_index] == " ":
            board[row][column_index] = player_mark
            return row  # Return the row where the checker was placed

def check_win(board, row, col, player_mark):
    """Checks for a win horizontally, vertically, and diagonally."""

    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_mark:
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
            if board[r][c] == player_mark:
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
            if board[r][c] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def is_board_full(board):
    """Checks if the board is full."""
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def main():
    """Main game loop."""
    board = create_board()
    player_turn = random.randint(0, PLAYERS - 1)  # Randomly choose starting player

    print_board(board)  # Print initial board

    while True:
        player_mark = PLAYER_MARKS[player_turn]
        column_index = get_player_move(board, player_mark)  # Get player move

        row = drop_checker(board, column_index, player_mark)  # Drop the checker
        print_board(board)  # Print updated board

        if check_win(board, row, column_index, player_mark):  # Check for win
            print(f"Player {player_mark} won!")
            break

        if is_board_full(board):  # Check for draw
            print("It's a draw!")
            break

        player_turn = (player_turn + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```