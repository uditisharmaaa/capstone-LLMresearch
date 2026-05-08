# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 173
# filename        : gen_0173_gemini_13.py
# timestamp       : 2026-04-06T10:10:32Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1262
# tokens_total    : 1636
# cost_usd        : 0.000542
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
PLAYER_TOKENS = ["X", "O"]


def create_board():
    """Creates an empty Connect 4 board."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board


def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for row in board:
        row_str = "+"
        for _ in range(COLS):
            row_str += "---+"
        print(row_str)
        row_str = "|"
        for cell in row:
            row_str += " " + cell + " |"
        print(row_str)
    row_str = "+"
    for _ in range(COLS):
        row_str += "---+"
    print(row_str)


def get_player_move(player_token, board):
    """Gets a valid move from the player."""
    while True:
        column_str = input(f"Player {player_token}, enter column (A-G): ").upper()

        if len(column_str) != 1 or column_str < 'A' or column_str > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        try:
            column = ord(column_str) - ord('A')
        except TypeError:
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        if column < 0 or column >= COLS:
            print("Invalid input. Please enter a letter between A and G.")
            continue

        if is_column_full(board, column):
            print("That column is full. Please choose another.")
            continue

        return column


def is_column_full(board, column):
    """Checks if a column is full."""
    return board[0][column] != " "


def drop_checker(board, column, player_token):
    """Drops the player's checker into the lowest available row in the column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player_token
            return


def check_win(board, player_token):
    """Checks if the current player has won."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == player_token and
                    board[row][col + 1] == player_token and
                    board[row][col + 2] == player_token and
                    board[row][col + 3] == player_token):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if (board[row][col] == player_token and
                    board[row + 1][col] == player_token and
                    board[row + 2][col] == player_token and
                    board[row + 3][col] == player_token):
                return True

    # Check positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == player_token and
                    board[row + 1][col + 1] == player_token and
                    board[row + 2][col + 2] == player_token and
                    board[row + 3][col + 3] == player_token):
                return True

    # Check negative diagonal
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if (board[row][col] == player_token and
                    board[row + 1][col - 1] == player_token and
                    board[row + 2][col - 2] == player_token and
                    board[row + 3][col - 3] == player_token):
                return True

    return False


def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)  # Randomly choose starting player

    print_board(board)

    while True:
        player_token = PLAYER_TOKENS[current_player]
        column = get_player_move(player_token, board)
        drop_checker(board, column, player_token)
        print_board(board)

        if check_win(board, player_token):
            print(f"Player {player_token} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYERS  # Switch to the next player


if __name__ == "__main__":
    main()
```