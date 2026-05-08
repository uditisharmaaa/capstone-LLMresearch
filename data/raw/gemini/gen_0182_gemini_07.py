# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 182
# filename        : gen_0182_gemini_07.py
# timestamp       : 2026-04-06T10:12:30Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 380
# tokens_output   : 1326
# tokens_total    : 1706
# cost_usd        : 0.000568
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

```python
import os
import random

# Define constant global variables for board dimensions and number of players
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Function to create the Connect 4 board
def create_board():
    """Creates a 2D list representing the Connect 4 board."""
    board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

# Function to print the board
def print_board(board):
    """Prints the Connect 4 board to the console."""
    os.system('clear')  # Clear the screen

    # Print column labels
    print("  ", end="")
    for i in range(BOARD_WIDTH):
        print(chr(ord('A') + i), end="   ")  # A, B, C, ...
    print()

    # Print the board with separators
    for row in board:
        print("+---" * BOARD_WIDTH + "+")
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print()
    print("+---" * BOARD_WIDTH + "+")


# Function to check if a column is full
def is_column_full(board, column):
    """Checks if the specified column is full."""
    return board[0][column] != ' '

# Function to drop a checker into the board
def drop_checker(board, column, player):
    """Drops the player's checker into the specified column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            return row  # Return the row where the checker was placed
    return -1  # Should not reach here if column is not full


# Function to check for a win
def check_win(board, row, col, player):
    """Checks for a win horizontally, vertically, and diagonally."""

    # Check horizontal
    count = 0
    for c in range(BOARD_WIDTH):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(BOARD_HEIGHT):
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
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
        if 0 <= r < BOARD_HEIGHT and 0 <= c < BOARD_WIDTH:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

# Function to check for a draw
def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False  # If there's an empty cell, not a draw
    return True

# Function to get player input
def get_player_move(board, player):
    """Gets the player's move, validates it, and returns the column index."""
    while True:
        move = input(f"Player {player}, enter column (A-G): ").upper()
        if not move.isalpha() or len(move) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(move) - ord('A')  # Convert letter to column index
        if 0 <= column < BOARD_WIDTH:
            if not is_column_full(board, column):
                return column
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid column. Choose a column between A and G.")

# Main game function
def play_connect_4():
    """Main function to play the Connect 4 game."""
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)  # Randomly choose the first player

    print_board(board)  # Print the initial board

    while True:
        # Get player's move
        column = get_player_move(board, current_player)

        # Drop the checker
        row = drop_checker(board, column, current_player)

        # Print the updated board
        print_board(board)

        # Check for a win
        if check_win(board, row, column, current_player):
            print(f"Player {current_player} won!")
            break

        # Check for a draw
        if check_draw(board):
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = players[1 - players.index(current_player)] # Switch player



# Start the game
if __name__ == "__main__":
    play_connect_4()
```