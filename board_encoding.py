#!/usr/bin/env python3
"""board_encoding.py"""


def decode_board(board_int: int) -> str:
    symbols = ["0", "1", "2"]  # 0 is blank, 1 is X and 2 is O
    board_str = ""  # board string
    for _ in range(9):
        digit = board_int % 3
        board_str = symbols[digit] + board_str  # assigns the digits to board symbols
        board_int //= 3
    return board_str


"""draw the tic tac toe board"""

def draw_board(board_str: str) -> None:
    for i in range(0, 9, 3):
        print(f"[ {board_str[i]}  {board_str[i+1]}  {board_str[i+2]} ]")
    # modified from ChatGPT


def main() -> None:
    encoded_boards = [2271, 1638, 12065]  # number(s) to be encoded
    for board_int in encoded_boards:
        print("Board Number:", board_int)
        draw_board(decode_board(board_int))  # draws the encoded board
        print()


if __name__ == "__main__":
    main()

# code is supplemented by ChatGPT and QIS101 workspace files
