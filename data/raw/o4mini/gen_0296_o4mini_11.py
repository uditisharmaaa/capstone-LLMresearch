# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 296
# filename        : gen_0296_o4mini_11.py
# timestamp       : 2026-05-07T17:02:37Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 958
# tokens_total    : 1345
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

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_CELL = ' '

def create_board():
    """
    Create a 2D board initialized with empty spaces.
    Returns:
        list: A 2D list representing the game board.
    """
    return [[EMPTY_CELL for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """
    Prints the Connect 4 board with column labels.
    Args:
        board (list): The game board to print.
    """
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def get_player_input(board, player):
    """
    Prompt the player to choose a column and validate the input.
    Args:
        board (list): The game board.
        player (str): The current player's checker ("X" or "O").
    Returns:
        int: The valid column index chosen by the player.
    """
    while True:
        choice = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if choice in COLUMN_LABELS:
            col = COLUMN_LABELS.index(choice)
            if board[0][col] == EMPTY_CELL:
                return col
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, col, player):
    """
    Drop the player's checker into the chosen column.
    Args:
        board (list): The game board.
        col (int): The column index.
        player (str): The current player's checker ("X" or "O").
    """
    for row in reversed(board):
        if row[col] == EMPTY_CELL:
            row[col] = player
            break

def check_winner(board, player):
    """
    Check if the current player has won the game.
    Args:
        board (list): The game board.
        player (str): The current player's checker ("X" or "O").
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for row in board:
        for col in range(COLS - 3):
            if all(row[col + i] == player for i in range(4)):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonals (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonals (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_draw(board):
    """
    Check if the board is full and no winner exists.
    Args:
        board (list): The game board.
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return all(cell != EMPTY_CELL for row in board for cell in row)

def play_connect4():
    """
    Main function to play the Connect 4 game.
    """
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    print_board(board)

    while True:
        col = get_player_input(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        elif is_draw(board):
            print("The game is a draw!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    play_connect4()
```