# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 276
# filename        : gen_0276_gemini_11.py
# timestamp       : 2026-04-06T10:28:32Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 375
# tokens_output   : 1497
# tokens_total    : 1872
# cost_usd        : 0.000636
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

# Constant global variables
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    """
    Creates a 2D list representing the Connect 4 board.
    
    Returns:
        list[list[str]]: A 2D list initialized with spaces, representing the board.
    """
    board = []
    for _ in range(BOARD_HEIGHT):
        board.append([" "] * BOARD_WIDTH)
    return board

def print_board(board):
    """
    Prints the Connect 4 board with column labels.
    
    Args:
        board (list[list[str]]): The 2D list representing the board.
    """
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---" * BOARD_WIDTH + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * BOARD_WIDTH + "+")

def clear_screen():
    """
    Clears the console screen.
    """
    os.system('clear')

def get_player_move(board, player):
    """
    Gets a valid move from the player.
    
    Args:
        board (list[list[str]]): The 2D list representing the board.
        player (str): The current player's checker ("X" or "O").
    
    Returns:
        int: The column index (0-6) chosen by the player.
    """
    while True:
        column_letter = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_letter.isalpha() or len(column_letter) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue
        
        try:
            column_index = ord(column_letter) - ord('A')
            if 0 <= column_index < BOARD_WIDTH:
                if board[0][column_index] == " ":
                    return column_index
                else:
                    print("Column is full. Choose another column.")
            else:
                print("Invalid column. Please enter a letter A-G.")
        except ValueError:
            print("Invalid input. Please enter a letter A-G.")

def drop_checker(board, column_index, player):
    """
    Drops the player's checker into the specified column.
    
    Args:
        board (list[list[str]]): The 2D list representing the board.
        column_index (int): The index of the column to drop the checker into.
        player (str): The player's checker ("X" or "O").
    """
    for row_index in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row_index][column_index] == " ":
            board[row_index][column_index] = player
            return

def check_win(board, player):
    """
    Checks if the given player has won the game.
    
    Args:
        board (list[list[str]]): The 2D list representing the board.
        player (str): The player's checker ("X" or "O").
    
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player):
                return True

    # Check vertical
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if (board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(3, BOARD_WIDTH):
            if (board[row][col] == player and
                board[row+1][col-1] == player and
                board[row+2][col-2] == player and
                board[row+3][col-3] == player):
                return True

    return False

def check_draw(board):
    """
    Checks if the board is full, indicating a draw.
    
    Args:
        board (list[list[str]]): The 2D list representing the board.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """
    Main function to run the Connect 4 game.
    """
    board = create_board()
    players = [PLAYER_X, PLAYER_O]
    current_player = random.choice(players)

    clear_screen()
    print_board(board)

    while True:
        column_index = get_player_move(board, current_player)
        drop_checker(board, column_index, current_player)

        clear_screen()
        print_board(board)

        if check_win(board, current_player):
            print(f"{current_player} won!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = players[(players.index(current_player) + 1) % NUM_PLAYERS]

if __name__ == "__main__":
    main()
```