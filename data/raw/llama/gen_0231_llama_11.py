# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 231
# filename        : gen_0231_llama_11.py
# timestamp       : 2026-04-06T09:37:34Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 390
# tokens_output   : 1143
# tokens_total    : 1533
# cost_usd        : 0.001060
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

# Global constants
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

def create_board():
    """
    Create a 2D board with the specified number of columns and rows,
    initialized with spaces.
    
    Returns:
        A 2D list representing the game board.
    """
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    """
    Print the game board with column labels A through G.
    
    Args:
        board (list): A 2D list representing the game board.
    """
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

def get_player_move(player):
    """
    Get the player's move, validating the input to ensure it is a letter
    between A and G (inclusive) and that the chosen column is not full.
    
    Args:
        player (int): The current player (1 or 2).
    
    Returns:
        The column index of the player's move.
    """
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please choose a different column.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, player, col):
    """
    Drop the player's checker into the lowest available row in the chosen column.
    
    Args:
        board (list): A 2D list representing the game board.
        player (int): The current player (1 or 2).
        col (int): The column index of the player's move.
    
    Returns:
        The row index where the checker was dropped.
    """
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = 'X' if player == 1 else 'O'
            return row

def check_win(board, player, row, col):
    """
    Check if the player has won by looking for four in a row horizontally,
    vertically, or diagonally.
    
    Args:
        board (list): A 2D list representing the game board.
        player (int): The current player (1 or 2).
        row (int): The row index where the checker was dropped.
        col (int): The column index of the player's move.
    
    Returns:
        True if the player has won, False otherwise.
    """
    checker = 'X' if player == 1 else 'O'
    
    # Check horizontal
    count = 0
    for c in range(BOARD_COLS):
        if board[row][c] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    # Check vertical
    count = 0
    for r in range(BOARD_ROWS):
        if board[r][col] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    # Check diagonal (top-left to bottom-right)
    count = 0
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if r - row == c - col and board[r][c] == checker:
                count += 1
                if count == 4:
                    return True
            elif r - row == c - col:
                count = 0
    
    # Check diagonal (bottom-left to top-right)
    count = 0
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if r - row == col - c and board[r][c] == checker:
                count += 1
                if count == 4:
                    return True
            elif r - row == col - c:
                count = 0
    
    return False

def main():
    """
    The main game loop.
    """
    global board
    board = create_board()
    print_board(board)
    
    players = ['X', 'O']
    current_player = random.randint(0, 1)
    
    while True:
        col = get_player_move(current_player + 1)
        row = drop_checker(board, current_player + 1, col)
        print_board(board)
        
        if check_win(board, current_player + 1, row, col):
            print(f"Player {current_player + 1} won!")
            break
        
        # Check for draw
        if all(board[0][c]!= ' ' for c in range(BOARD_COLS)):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```