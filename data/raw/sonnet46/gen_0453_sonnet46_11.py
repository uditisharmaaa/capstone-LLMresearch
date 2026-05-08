# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 453
# filename        : gen_0453_sonnet46_11.py
# timestamp       : 2026-05-07T22:41:18Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 416
# tokens_output   : 2098
# tokens_total    : 2514
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

import os
import random

NUM_PLAYERS = 2
NUM_COLS = 7
NUM_ROWS = 6
PLAYERS = ["X", "O"]
COL_LABELS = ["A", "B", "C", "D", "E", "F", "G"]


def create_board():
    """
    Create and return a 2D list representing the Connect 4 board.

    The board is initialized with spaces, where each cell contains a single
    space character. The board is structured as a list of rows, where each
    row is a list of column values.

    Returns:
        list: A 2D list of dimensions NUM_ROWS x NUM_COLS, filled with spaces.
    """
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]


def print_board(board):
    """
    Clear the screen and print the current state of the Connect 4 board.

    The board is printed with column labels A through G at the top, followed
    by rows separated by horizontal dividers. Each cell is displayed within
    vertical bars.

    Args:
        board (list): A 2D list representing the current state of the board.

    Returns:
        None
    """
    os.system("clear")
    print("   " + "   ".join(COL_LABELS))
    for row in board:
        print("+---" * NUM_COLS + "+")
        print("|" + "|".join(f" {cell} " for cell in row) + "|")
    print("+---" * NUM_COLS + "+")


def get_player_input(board, player):
    """
    Prompt the current player to choose a column and validate their input.

    This function continuously asks the player for input until a valid column
    is provided. Valid input must be a single uppercase letter between A and G
    that corresponds to a column that is not already full.

    Validation rules:
        - Input must be a single alphabetic character.
        - The character must be one of the valid column labels (A through G).
        - The chosen column must not be full (i.e., the top row must be empty).

    Args:
        board (list): A 2D list representing the current state of the board.
        player (str): The current player's checker symbol ("X" or "O").

    Returns:
        int: The zero-based column index corresponding to the player's choice.
    """
    while True:
        user_input = input(f"Player {player}, choose a column (A-G): ")
        if not user_input.isalpha():
            print("Invalid input. Please enter a letter between A and G.")
            continue
        user_input = user_input.upper()
        if user_input not in COL_LABELS:
            print("Invalid column. Please enter a letter between A and G.")
            continue
        col_index = COL_LABELS.index(user_input)
        if board[0][col_index] != " ":
            print("That column is full. Please choose another column.")
            continue
        return col_index


def drop_checker(board, col, player):
    """
    Drop a player's checker into the specified column of the board.

    The checker falls to the lowest available row in the given column,
    simulating gravity. The function searches from the bottom row upward
    and places the checker in the first empty cell found.

    Args:
        board (list): A 2D list representing the current state of the board.
        col (int): The zero-based column index where the checker is to be dropped.
        player (str): The current player's checker symbol ("X" or "O").

    Returns:
        None
    """
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return


def check_winner(board, player):
    """
    Check whether the specified player has won the game.

    A player wins if they have four consecutive checkers in a row horizontally,
    vertically, or diagonally (both directions). This function checks all four
    win conditions across the entire board.

    Win conditions checked:
        - Horizontal: Four in a row across any row.
        - Vertical: Four in a column going downward.
        - Diagonal (top-left to bottom-right): Four along a descending diagonal.
        - Diagonal (top-right to bottom-left): Four along an ascending diagonal.

    Args:
        board (list): A 2D list representing the current state of the board.
        player (str): The player's checker symbol to check for a win ("X" or "O").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False


def check_draw(board):
    """
    Check whether the game has ended in a draw.

    A draw occurs when all cells on the board are filled and no player has won.
    This function checks if there are any remaining empty cells in the top row,
    since a full top row means the entire board is full.

    Args:
        board (list): A 2D list representing the current state of the board.

    Returns:
        bool: True if the board is completely full (draw), False otherwise.
    """
    return all(board[0][col] != " " for col in range(NUM_COLS))


def select_starting_player():
    """
    Randomly select and return which player goes first.

    This function uses Python's random module to randomly choose one of the
    two player symbols from the PLAYERS list. The result determines which
    player takes the first turn at the beginning of the game.

    Returns:
        str: The checker symbol ("X" or "O") of the player who goes first.
    """
    return random.choice(PLAYERS)


def switch_player(current_player):
    """
    Switch and return the other player's symbol.

    Given the current player's checker symbol, this function returns the
    symbol of the opposing player. This is used to alternate turns between
    the two players after each valid move.

    Args:
        current_player (str): The current player's checker symbol ("X" or "O").

    Returns:
        str: The opposing player's checker symbol.
    """
    return "O" if current_player == "X" else "X"


def play_game():
    """
    Run the main game loop for Connect 4.

    This function orchestrates the entire Connect 4 game from start to finish.
    It initializes the board, randomly selects the starting player, and then
    enters a loop where each iteration represents one player's turn.

    Each turn involves:
        1. Printing the current board state.
        2. Prompting the current player for a valid column input.
        3. Dropping their checker into the chosen column.
        4. Checking if the current player has won.
        5. Checking if the board is full (draw condition).
        6. Switching to the other player if the game continues.

    The game ends when a player wins or the board is full with no winner.
    A final message is printed declaring the winner or announcing a draw.

    Returns:
        None
    """
    board = create_board()
    current_player = select_starting_player()

    while True:
        print_board(board)
        col = get_player_input(board, current_player)
        drop_checker(board, col, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)


play_game()