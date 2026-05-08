# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 201
# filename        : gen_0201_sonnet_11.py
# timestamp       : 2026-04-06T10:15:19Z
# model           : anthropic/claude-3.7-sonnet
# model_short     : sonnet
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 416
# tokens_output   : 1774
# tokens_total    : 2190
# cost_usd        : 0.027858
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

# Global constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
PLAYER_TOKENS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_CELL = ' '
WIN_COUNT = 4

def create_board():
    """
    Creates a new Connect 4 board.
    
    Returns:
        list: A 2D list representing the board, initialized with empty spaces.
    """
    return [[EMPTY_CELL for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """
    Prints the current state of the board.
    
    Args:
        board (list): The 2D list representing the board.
    """
    os.system('clear')
    # Print column labels
    print('   ' + '   '.join(COLUMN_LABELS) + '')
    
    # Print board
    for row in board:
        print('+---+---+---+---+---+---+---+')
        print('| ' + ' | '.join(row) + ' |')
    
    # Print bottom border
    print('+---+---+---+---+---+---+---+')

def is_valid_move(board, column_idx):
    """
    Checks if a move is valid.
    
    Args:
        board (list): The 2D list representing the board.
        column_idx (int): The index of the column to check.
        
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Check if column is within bounds
    if column_idx < 0 or column_idx >= COLUMNS:
        return False
    
    # Check if the top cell in the column is empty
    return board[0][column_idx] == EMPTY_CELL

def get_next_open_row(board, column_idx):
    """
    Finds the next available row in a column.
    
    Args:
        board (list): The 2D list representing the board.
        column_idx (int): The index of the column to check.
        
    Returns:
        int: The index of the next available row, or -1 if the column is full.
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][column_idx] == EMPTY_CELL:
            return row
    return -1

def drop_checker(board, column_idx, player_token):
    """
    Drops a checker into the specified column.
    
    Args:
        board (list): The 2D list representing the board.
        column_idx (int): The index of the column to drop the checker.
        player_token (str): The token of the current player.
        
    Returns:
        bool: True if the checker was dropped successfully, False otherwise.
    """
    row_idx = get_next_open_row(board, column_idx)
    if row_idx != -1:
        board[row_idx][column_idx] = player_token
        return True
    return False

def check_win(board, player_token):
    """
    Checks if the current player has won.
    
    Args:
        board (list): The 2D list representing the board.
        player_token (str): The token of the current player.
        
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - WIN_COUNT + 1):
            if all(board[row][col + i] == player_token for i in range(WIN_COUNT)):
                return True
    
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - WIN_COUNT + 1):
            if all(board[row + i][col] == player_token for i in range(WIN_COUNT)):
                return True
    
    # Check diagonal (down-right)
    for row in range(ROWS - WIN_COUNT + 1):
        for col in range(COLUMNS - WIN_COUNT + 1):
            if all(board[row + i][col + i] == player_token for i in range(WIN_COUNT)):
                return True
    
    # Check diagonal (up-right)
    for row in range(WIN_COUNT - 1, ROWS):
        for col in range(COLUMNS - WIN_COUNT + 1):
            if all(board[row - i][col + i] == player_token for i in range(WIN_COUNT)):
                return True
    
    return False

def is_board_full(board):
    """
    Checks if the board is full.
    
    Args:
        board (list): The 2D list representing the board.
        
    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(board[0][col] != EMPTY_CELL for col in range(COLUMNS))

def get_player_move(board):
    """
    Gets the player's move.
    
    Args:
        board (list): The 2D list representing the board.
        
    Returns:
        int: The index of the column chosen by the player.
    """
    while True:
        try:
            column_letter = input("Choose a column (A-G): ").upper()
            if len(column_letter) != 1 or not column_letter.isalpha():
                print("Please enter a single letter.")
                continue
                
            if column_letter not in COLUMN_LABELS:
                print("Please enter a letter between A and G.")
                continue
                
            column_idx = COLUMN_LABELS.index(column_letter)
            
            if not is_valid_move(board, column_idx):
                print("That column is full. Choose another column.")
                continue
                
            return column_idx
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def play_game():
    """
    Main function to play the Connect 4 game.
    """
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False
    
    print_board(board)
    
    while not game_over:
        player_token = PLAYER_TOKENS[current_player]
        print(f"Player {player_token}'s turn")
        
        column_idx = get_player_move(board)
        drop_checker(board, column_idx, player_token)
        
        print_board(board)
        
        # Check for win
        if check_win(board, player_token):
            print(f"Player {player_token} won!")
            game_over = True
            continue
        
        # Check for draw
        if is_board_full(board):
            print("It's a draw!")
            game_over = True
            continue
        
        # Switch player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    play_game()