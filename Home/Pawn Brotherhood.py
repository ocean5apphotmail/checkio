#  Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions (for example Number of possible chess games at the end of the n-th plies. ) For this mission, we will examine the movements and behavior of chess pawns.
#
# Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row number than the square they currently occupy.
#
# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
#
#  You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
#
# Input: Placed pawns coordinates as a set of strings.
#
# Output: The number of safe pawns as a integer.
#
# Example:
#
# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
# safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#  How it is used: For a game AI one of the important tasks is the ability to estimate game state. This concept will show how you can do this on the simple chess figures positions.
#
# Precondition:
# 0 < pawns ≤ 8
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-pawn-brotherhood { 22 }

def lower_rank(rank: str) -> str:
    if rank == '8':
        return '7'
    elif rank == '7':
        return '6'
    elif rank == '6':
        return '5'
    elif rank == '5':
        return '4'
    elif rank == '4':
        return '3'
    elif rank == '3':
        return '2'
    elif rank == '2':
        return '1'
    else:
        return 'on safe'


def left_file(file: str) -> str:
    if file == 'h':
        return 'g'
    elif file == 'g':
        return 'f'
    elif file == 'f':
        return 'e'
    elif file == 'e':
        return 'd'
    elif file == 'd':
        return 'c'
    elif file == 'c':
        return 'b'
    elif file == 'b':
        return 'a'
    else:
        return 'on safe'


def right_file(file: str) -> str:
    if file == 'a':
        return 'b'
    elif file == 'b':
        return 'c'
    elif file == 'c':
        return 'd'
    elif file == 'd':
        return 'e'
    elif file == 'e':
        return 'f'
    elif file == 'f':
        return 'g'
    elif file == 'g':
        return 'h'
    else:
        return 'on safe'


def lower_left(position: str) -> str:
    if 'a' in position or '1' in position:
        return 'no safe'
    return left_file(position[0]) + lower_rank(position[1])


def lower_right(position: str) -> str:
    if 'h' in position or '1' in position:
        return 'no safe'
    return right_file(position[0]) + lower_rank(position[1])


def safe_pawns(pawns: set) -> int:
    safe = 0
    for p in pawns:
        if lower_left(p) in pawns or lower_right(p) in pawns:
            safe = safe + 1
    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
