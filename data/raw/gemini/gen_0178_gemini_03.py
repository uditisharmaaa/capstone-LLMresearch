# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 178
# filename        : gen_0178_gemini_03.py
# timestamp       : 2026-04-06T10:11:34Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1249
# tokens_total    : 1624
# cost_usd        : 0.000537
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

# Define constant global variables
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_1 = "X"
PLAYER_2 = "O"

def create_board():
    """Creates a 2D list representing the Connect 4 board."""
    return [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board):
    """Prints the Connect 4 board to the console with column labels."""
    os.system('clear')  # Clear the console
    print("  A   B   C   D   E   F   G")  # Print column labels
    for row in range(BOARD_HEIGHT):
        print("+---+---+---+---+---+---+---+")  # Print row separator
        print("| " + " | ".join(board[row]) + " |")  # Print row content
    print("+---+---+---+---+---+---+---+")  # Print bottom row separator

def get_player_move(player, board):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()

        if len(column_input) != 1 or column_input < 'A' or column_input > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue

        column = ord(column_input) - ord('A')  # Convert letter to column index

        if is_column_full(board, column):
            print("That column is full. Please choose another column.")
            continue

        return column

def is_column_full(board, column):
    """Checks if a column is full."""
    return board[0][column] != ' '

def drop_checker(board, column, player):
    """Drops the checker into the lowest available row in the chosen column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            return True
    return False  # Should not reach here if input is validated correctly

def check_win(board, player):
    """Checks for a win in horizontal, vertical, and diagonal directions."""
    # Check horizontal
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player):
                return True

    # Check vertical
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if (board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(3, BOARD_WIDTH):
            if (board[row][col] == player and
                board[row + 1][col - 1] == player and
                board[row + 2][col - 2] == player and
                board[row + 3][col - 3] == player):
                return True

    return False

def is_board_full(board):
    """Checks if the board is full (draw)."""
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == ' ':
                return False  # Found an empty space
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()  # Create the game board
    current_player = random.choice([PLAYER_1, PLAYER_2])  # Randomly choose the first player

    print_board(board)  # Print the initial board

    while True:
        column = get_player_move(current_player, board)  # Get the player's move
        drop_checker(board, column, current_player) # Drop the checker into the board
        print_board(board)  # Print the updated board

        if check_win(board, current_player):  # Check for a win
            print(f"Player {current_player} won!")
            break

        if is_board_full(board):  # Check for a draw
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

if __name__ == "__main__":
    main()
```