# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 435
# filename        : gen_0435_opus_08.py
# timestamp       : 2026-05-07T22:34:31Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 418
# tokens_output   : 1531
# tokens_total    : 1949
# cost_usd        : 0.121095
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
#   Write with a focus on code readability over brevity.
# ====================================================================

import os
import random

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
PLAYER_CHECKERS = ['X', 'O']


def create_board():
    board = []
    for row in range(BOARD_HEIGHT):
        new_row = []
        for col in range(BOARD_WIDTH):
            new_row.append(' ')
        board.append(new_row)
    return board


def clear_screen():
    os.system('clear')


def print_board(board):
    clear_screen()
    
    header = "   "
    for label in COLUMN_LABELS:
        header += label + "   "
    print(header)
    
    separator = "+"
    for col in range(BOARD_WIDTH):
        separator += "---+"
    
    for row in range(BOARD_HEIGHT):
        print(separator)
        
        row_string = "|"
        for col in range(BOARD_WIDTH):
            row_string += " " + board[row][col] + " |"
        print(row_string)
    
    print(separator)


def get_column_index(column_letter):
    return ord(column_letter) - ord('A')


def is_valid_column_letter(input_string):
    if len(input_string) != 1:
        return False
    
    if not input_string.isalpha():
        return False
    
    if input_string not in COLUMN_LABELS:
        return False
    
    return True


def is_column_full(board, column_index):
    return board[0][column_index] != ' '


def get_player_move(board, player_checker):
    while True:
        user_input = input(f"Player {player_checker}, choose a column (A-G): ")
        
        user_input = user_input.strip().upper()
        
        if not is_valid_column_letter(user_input):
            print("Invalid input. Please enter a letter from A to G.")
            continue
        
        column_index = get_column_index(user_input)
        
        if is_column_full(board, column_index):
            print("That column is full. Please choose a different column.")
            continue
        
        return column_index


def drop_checker(board, column_index, player_checker):
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column_index] == ' ':
            board[row][column_index] = player_checker
            return row
    
    return -1


def check_horizontal_win(board, row, col, player_checker):
    count = 0
    
    for c in range(BOARD_WIDTH):
        if board[row][c] == player_checker:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    
    return False


def check_vertical_win(board, row, col, player_checker):
    count = 0
    
    for r in range(BOARD_HEIGHT):
        if board[r][col] == player_checker:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    
    return False


def check_diagonal_win(board, row, col, player_checker):
    for start_row in range(BOARD_HEIGHT - 3):
        for start_col in range(BOARD_WIDTH - 3):
            if (board[start_row][start_col] == player_checker and
                board[start_row + 1][start_col + 1] == player_checker and
                board[start_row + 2][start_col + 2] == player_checker and
                board[start_row + 3][start_col + 3] == player_checker):
                return True
    
    for start_row in range(3, BOARD_HEIGHT):
        for start_col in range(BOARD_WIDTH - 3):
            if (board[start_row][start_col] == player_checker and
                board[start_row - 1][start_col + 1] == player_checker and
                board[start_row - 2][start_col + 2] == player_checker and
                board[start_row - 3][start_col + 3] == player_checker):
                return True
    
    return False


def check_win(board, row, col, player_checker):
    if check_horizontal_win(board, row, col, player_checker):
        return True
    
    if check_vertical_win(board, row, col, player_checker):
        return True
    
    if check_diagonal_win(board, row, col, player_checker):
        return True
    
    return False


def is_board_full(board):
    for col in range(BOARD_WIDTH):
        if board[0][col] == ' ':
            return False
    return True


def select_starting_player():
    return random.randint(0, NUM_PLAYERS - 1)


def play_game():
    board = create_board()
    
    current_player_index = select_starting_player()
    
    print_board(board)
    
    game_over = False
    
    while not game_over:
        current_checker = PLAYER_CHECKERS[current_player_index]
        
        column_index = get_player_move(board, current_checker)
        
        row_placed = drop_checker(board, column_index, current_checker)
        
        print_board(board)
        
        if check_win(board, row_placed, column_index, current_checker):
            print(f"{current_checker} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    play_game()