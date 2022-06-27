#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""


import sys
import itertools


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be an integer greater than or equal to 4.")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)
    print("Found %d solutions." % len(solutions))
    for solution in solutions:
        print(solution)


def solve(board, row, solutions):
    """Solve the N-queens puzzle.

    Args:
        board (list): A list of lists representing the chessboard.
        row (int): The current row.
        solutions (list): A list of lists containing solutions.
    """
    if row == len(board):
        solutions.append(board)
        return

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve(board, row + 1, solutions)
            board[row][col] = 0


def is_valid(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True
