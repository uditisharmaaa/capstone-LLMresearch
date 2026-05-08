# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 371
# filename        : gen_0371_o4mini_11.py
# timestamp       : 2026-05-07T17:51:59Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 1053
# tokens_total    : 1440
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
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_SLOT = ' '

def clear_screen():
    """Clears the console screen."""
    os.system('clear')

def create_board():
    """
    Creates and initializes the game board.
    
    Returns:
        list: A 2D list representing the board, initialized with empty spaces.
    """
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """
    Prints the current state of the board to the console.
    
    Args:
        board (list): The game board to print.
    """
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_player_input(board, player):
    """
    Gets and validates the player's move.
    
    Args:
        board (list): The current game board.
        player (str): The player's symbol ("X" or "O").
    
    Returns:
        int: The column index where the player wants to drop their checker.
    """
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if move not in COLUMN_LABELS:
            print("Invalid input. Enter a letter between A and G.")
            continue
        column = COLUMN_LABELS.index(move)
        if board[0][column] != EMPTY_SLOT:
            print("Column is full. Choose a different column.")
            continue
        return column

def drop_checker(board, column, player):
    """
    Drops the player's checker into the chosen column.
    
    Args:
        board (list): The current game board.
        column (int): The column index where the checker is dropped.
        player (str): The player's symbol ("X" or "O").
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY_SLOT:
            board[row][column] = player
            break

def check_winner(board, player):
    """
    Checks if the given player has won the game.
    
    Args:
        board (list): The current game board.
        player (str): The player's symbol ("X" or "O").
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal win
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical win
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right) win
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right) win
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_draw(board):
    """
    Checks if the game is a draw (no empty slots left).
    
    Args:
        board (list): The current game board.
    
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return all(board[0][col] != EMPTY_SLOT for col in range(COLUMNS))

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]

    print_board(board)
    print(f"Player {current_player} goes first!")

    while True:
        # Get and process the current player's move
        column = get_player_input(board, current_player)
        drop_checker(board, column, current_player)
        print_board(board)

        # Check for a win or draw
        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        if is_draw(board):
            print("The game is a draw!")
            break

        # Switch to the other player
        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    main()
```