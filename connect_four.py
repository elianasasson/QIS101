#!/usr/bin/env python3
"""connect_four.py"""

def check_ray(col: int, board: list[list[int]], row: int ) -> bool: 
    if col < 4 and ( # checking horizontal right
    board[row][col] == board[row][col + 1 ]
    and board[row][col] == board [row][col + 2]
    and board[row][col] == board [row][col + 3]
    ):
        return True

    if col > 2 and( # checking horizontal left
        board[row][col] == board [row][col - 1]
        and board[row][col] == board [row][col - 2]
        and board[row][col] == board [row][col - 3]
    ): 
            return True
    if row < 3 and col < 4 and ( # checking diagonal right downwards
        board[row][col] == board[row + 1][col + 1]
        and board[row][col] == board[row + 2][col + 2]
        and board[row][col] == board[row + 3][col + 3]
        ):
        return True

    if row < 3 and col > 2 and ( # checking diagonal left downwards
        board[row][col] == board[row + 1][col - 1]
        and board[row][col] == board[row + 2][col - 2]
        and board[row][col] == board[row + 3][col - 3]
        ):
        return True
    
    if row < 3 and ( # checking vertical downwards
    board[row][col] == board[row + 1][col]
    and board[row][col] == board[row + 2][col]
    and board[row][col] == board[row + 3][col]
    ):
        return True # code for diagonals and vertical are supplemented with help from chatgpt

    return False


def check_winner(player: int, board: list[list[int]]) -> bool:
    for row in range(6):
        for col in range(7):
            if board[row][col] ==  player and check_ray(col, board, row):
                return True
    return False

"""declare winner"""
def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")
    if check_winner(1, board):
        print( "Win: Player 1")
    else:
        if check_winner(2, board):
            print("Winner: Player 2")
        else:
            print("No Winner")
    print()

"""printing the winner"""
def main() -> None: # board 1
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [ # board 2
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [ # board 3
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
