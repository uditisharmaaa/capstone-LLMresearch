# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 393
# filename        : gen_0393_gemini25p_03.py
# timestamp       : 2026-05-07T18:00:49Z
# model           : @vertexai/gemini-2.5-pro
# model_short     : gemini25p
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 2996
# tokens_total    : 3371
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

# Import necessary libraries for clearing the screen and random selection
import os
import random

# --- Global Constants ---
# These constants define the game's properties and should not be changed during gameplay.
# Using constants makes the code easier to read and modify.

# Board dimensions
ROWS = 6
COLS = 7

# Player information
NUM_PLAYERS = 2
PLAYERS = ('X', 'O')  # Tuple of characters representing the players' checkers

def clear_screen():
    """Clears the console screen.
    
    Uses 'cls' for Windows and 'clear' for other operating systems (macOS, Linux).
    This improves the user experience by keeping the display clean.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    """Creates and returns an empty game board.
    
    The board is a 2D list (a list of lists) with dimensions ROWS x COLS.
    Each cell is initialized with a space character ' ' to indicate it's empty.
    """
    # Using a list comprehension for a concise way to build the 2D list.
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board

def print_board(board):
    """Prints the current state of the game board to the console.
    
    The board is formatted for readability with column labels (A-G) and borders.
    This function is called after the screen is cleared, before each turn.
    """
    # Print the column labels (A, B, C, ...)
    # '  '.join(...) creates the spacing between letters.
    print("   " + "   ".join([chr(ord('A') + c) for c in range(COLS)]))

    # Print the board rows with separators
    for r in range(ROWS):
        # Print the horizontal separator line
        print("+" + "---+" * COLS)
        # Print the row content, with each cell value padded by spaces
        row_str = "| " + " | ".join(board[r]) + " |"
        print(row_str)
    
    # Print the final bottom border of the board
    print("+" + "---+" * COLS)

def get_player_move(board, player):
    """Asks the current player for their move and validates it.
    
    Args:
        board: The current game board.
        player: The character ('X' or 'O') of the current player.
        
    Returns:
        