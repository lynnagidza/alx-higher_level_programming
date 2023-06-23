#!/usr/bin/python3
"""
N-Queens Puzzle Solver

This program solves the N-queens problem, which is the challenge of placing N
non-attacking queens on an N×N chessboard.

Usage:
    nqueens N

    - If the user called the program with the wrong number of arguments, it
    prints "Usage: nqueens N",
      followed by a new line, and exits with the status 1.
    - N must be an integer greater than or equal to 4.
      - If N is not an integer, it prints "N must be a number", followed by a
      new line, and exits with the status 1.
      - If N is smaller than 4, it prints "N must be at least 4", followed by
      a new line, and exits with the status 1.

The program prints every possible solution to the N-queens problem, with one
solution per line.
The solutions are printed in the format: [[row_1, col_1], [row_2, col_2], ...]

You are only allowed to import the sys module.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    n = len(board)

    for i in range(row):
        if board[i][col] == 1 or \
           (0 <= col - row + i < n and board[i][col - row + i] == 1) or \
           (0 <= col + row - i < n and board[i][col + row - i] == 1):
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-queens problem.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: List of all solutions to the N-queens problem.
    """
    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions


def backtrack(board, row, solutions):
    """
    Backtracking function to find solutions to the N-queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to consider.
        solutions (list): List to store the solutions.
    """
    n = len(board)

    if row == n:
        queens = [[i, j] for i in range(n)
                  for j in range(n) if board[i][j] == 1]
        solutions.append(queens)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            backtrack(board, row + 1, solutions)
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print the solutions to the N-queens problem.

    Args:
        solutions (list): List of solutions.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
