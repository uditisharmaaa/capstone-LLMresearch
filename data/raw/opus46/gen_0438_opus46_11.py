# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 438
# filename        : gen_0438_opus46_11.py
# timestamp       : 2026-05-07T22:35:26Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 416
# tokens_output   : 2367
# tokens_total    : 2783
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

ROWS = 6
COLS = 7
NUM_PLAYERS = 2

def create_board():
    """
    Create and return a 2D board for Connect 4.
    
    The board is represented as a list of lists, where each inner list
    represents a row. The board has ROWS rows and COLS columns.
    Each cell is initialized with a space character ' ' to indicate
    that it is empty.
    
    Returns:
        list: A 2D list of dimensions ROWS x COLS, filled with spaces.
    """
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(' ')
        board.append(row)
    return board


def print_board(board):
    """
    Clear the screen and print the current state of the Connect 4 board.
    
    The function first clears the terminal screen using os.system('clear'),
    then prints column labels A through G centered above each column,
    followed by the grid with horizontal and vertical separators.
    
    The board is printed in the following format:
       A   B   C   D   E   F   G
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    ...
    
    Args:
        board (list): A 2D list representing the game board, where each
                      cell contains ' ', 'X', or 'O'.
    """
    os.system('clear')
    header = " "
    for c in range(COLS):
        header += "  " + chr(ord('A') + c) + " "
    print(header)
    separator = "+" + "---+" * COLS
    for r in range(ROWS):
        print(separator)
        row_str = "|"
        for c in range(COLS):
            row_str += " " + board[r][c] + " |"
        print(row_str)
    print(separator)


def get_column_choice(board, player):
    """
    Prompt the current player to choose a column and validate the input.
    
    This function repeatedly asks the player for input until a valid
    column is chosen. A valid column must satisfy all of the following:
    - The input must be exactly one alphabetic character.
    - The character must be an uppercase letter between 'A' and 'G' (inclusive).
    - The chosen column must not be full (i.e., the top row of that column
      must contain a space).
    
    If the input is invalid for any reason, an appropriate error message
    is printed and the player is prompted again. The turn does NOT end
    on invalid input.
    
    Args:
        board (list): A 2D list representing the current game board.
        player (str): The current player's checker, either 'X' or 'O'.
    
    Returns:
        int: The column index (0-6) corresponding to the valid column chosen.
    """
    while True:
        choice = input("Player " + player + ", choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        choice = choice.upper()
        if choice < 'A' or choice > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = ord(choice) - ord('A')
        if board[0][col] != ' ':
            print("Column " + choice + " is full. Please choose another column.")
            continue
        return col


def drop_checker(board, col, player):
    """
    Drop a checker into the specified column of the board.
    
    The checker falls to the lowest available (empty) row in the given
    column, simulating gravity. This function assumes the column is not
    full (validation should be done before calling this function).
    
    Args:
        board (list): A 2D list representing the current game board.
        col (int): The column index (0-6) where the checker should be dropped.
        player (str): The current player's checker, either 'X' or 'O'.
    
    Returns:
        int: The row index where the checker was placed.
    """
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = player
            return r
    return -1


def check_win(board, player):
    """
    Check if the specified player has won the game.
    
    A player wins by having four of their checkers in a consecutive line,
    either horizontally, vertically, or diagonally (both directions).
    
    The function checks all possible four-in-a-row combinations on the
    board:
    - Horizontal: four consecutive cells in the same row.
    - Vertical: four consecutive cells in the same column.
    - Diagonal (down-right): four consecutive cells going from top-left
      to bottom-right.
    - Diagonal (down-left): four consecutive cells going from top-right
      to bottom-left.
    
    Args:
        board (list): A 2D list representing the current game board.
        player (str): The player's checker to check for, either 'X' or 'O'.
    
    Returns:
        bool: True if the player has four in a row, False otherwise.
    """
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == player and board[r][c + 1] == player and
                    board[r][c + 2] == player and board[r][c + 3] == player):
                return True

    # Check vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if (board[r][c] == player and board[r + 1][c] == player and
                    board[r + 2][c] == player and board[r + 3][c] == player):
                return True

    # Check diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == player and board[r + 1][c + 1] == player and
                    board[r + 2][c + 2] == player and board[r + 3][c + 3] == player):
                return True

    # Check diagonal (down-left)
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if (board[r][c] == player and board[r + 1][c - 1] == player and
                    board[r + 2][c - 2] == player and board[r + 3][c - 3] == player):
                return True

    return False


def is_board_full(board):
    """
    Check if the board is completely full with no empty spaces remaining.
    
    A board is considered full when every cell in the top row (row 0)
    contains a checker (either 'X' or 'O'). Since checkers drop to the
    lowest available position, if the top row is full, all rows below
    must also be full.
    
    Args:
        board (list): A 2D list representing the current game board.
    
    Returns:
        bool: True if the board is full, False if there is at least one
              empty cell remaining.
    """
    for c in range(COLS):
        if board[0][c] == ' ':
            return False
    return True


def main():
    """
    Main function to run the Connect 4 game.
    
    This function orchestrates the entire game flow:
    1. Creates a new empty board.
    2. Randomly selects which player ('X' or 'O') goes first.
    3. Displays the initial empty board.
    4. Enters the main game loop where players alternate turns:
       a. The current player is prompted to choose a column.
       b. The checker is dropped into the chosen column.
       c. The board is reprinted to show the updated state.
       d. The game checks for a win condition (four in a row).
       e. The game checks for a draw condition (board full).
       f. If neither, the turn passes to the other player.
    5. When the game ends (win or draw), an appropriate message is printed.
    
    The game supports exactly NUM_PLAYERS (2) players using checkers
    'X' and 'O'. The board has COLS (7) columns labeled A-G and
    ROWS (6) rows.
    """
    board = create_board()
    players = ['X', 'O']
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)

    while True:
        current_player = players[current_player_index]
        col = get_column_choice(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(current_player + " won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()
```