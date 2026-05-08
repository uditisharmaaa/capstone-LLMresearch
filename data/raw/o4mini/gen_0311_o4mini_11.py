# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 311
# filename        : gen_0311_o4mini_11.py
# timestamp       : 2026-05-07T17:20:57Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 1058
# tokens_total    : 1445
# cost_usd        : 0.000000
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

# Constants for the board dimensions and number of players
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2

# Initialize global variables for player symbols
PLAYER_SYMBOLS = ["X", "O"]

def clear_screen():
    """
    Clears the console screen.
    """
    os.system('clear')

def create_board():
    """
    Creates and initializes the Connect 4 board with spaces.

    Returns:
        list: A 2D list representing the empty board.
    """
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """
    Prints the current state of the board with column labels.

    Args:
        board (list): The current game board.
    """
    clear_screen()
    # Print column labels
    print("   " + "   ".join("ABCDEFG"))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_player_input(board, player_symbol):
    """
    Prompts the player to input a column letter and validates it.

    Args:
        board (list): The current game board.
        player_symbol (str): The symbol of the current player.

    Returns:
        int: The index of the chosen column.
    """
    while True:
        try:
            column = input(f"Player {player_symbol}, choose a column (A-G): ").strip().upper()
            if column not in "ABCDEFG" or len(column) != 1:
                print("Invalid input. Please choose a column between A and G.")
                continue
            column_index = ord(column) - ord("A")
            if board[0][column_index] != " ":
                print("Column is full. Please choose another column.")
                continue
            return column_index
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

def drop_checker(board, column, player_symbol):
    """
    Drops the player's checker into the chosen column.

    Args:
        board (list): The current game board.
        column (int): The index of the chosen column.
        player_symbol (str): The symbol of the current player.
    """
    for row in reversed(board):
        if row[column] == " ":
            row[column] = player_symbol
            break

def check_winner(board, player_symbol):
    """
    Checks if the current player has won the game.

    Args:
        board (list): The current game board.
        player_symbol (str): The symbol of the current player.

    Returns:
        bool: True if the player has won, otherwise False.
    """
    # Check horizontal wins
    for row in board:
        for col in range(COLUMNS - 3):
            if all(row[col + i] == player_symbol for i in range(4)):
                return True

    # Check vertical wins
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_symbol for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right) wins
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player_symbol for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right) wins
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player_symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    """
    Checks if the game is a draw (board is full with no winner).

    Args:
        board (list): The current game board.

    Returns:
        bool: True if the game is a draw, otherwise False.
    """
    return all(board[0][col] != " " for col in range(COLUMNS))

def main():
    """
    Main function to run the Connect 4 game.
    """
    board = create_board()
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    current_player_symbol = PLAYER_SYMBOLS[current_player_index]

    print_board(board)

    while True:
        column = get_player_input(board, current_player_symbol)
        drop_checker(board, column, current_player_symbol)
        print_board(board)

        if check_winner(board, current_player_symbol):
            print(f"Player {current_player_symbol} won!")
            break

        if is_draw(board):
            print("The game is a draw!")
            break

        # Switch to the next player
        current_player_index = (current_player_index + 1) % NUM_PLAYERS
        current_player_symbol = PLAYER_SYMBOLS[current_player_index]

if __name__ == "__main__":
    main()
```