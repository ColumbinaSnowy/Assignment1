"""
Codility Lesson 3 (Time Complexity) - FrogJmp
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

A frog starts at position X and wants to reach a position >= Y.
Each jump covers exactly D units. Return the minimum number of jumps.

Time: O(1)   Space: O(1)
"""


def solution(X, Y, D):
    # Distance the frog still has to cover
    distance = Y - X

    # We need ceil(distance / D) jumps.
    # (distance + D - 1) // D is integer ceiling division,
    # so we avoid floating-point rounding errors.
    return (distance + D - 1) // D


if __name__ == "__main__":
    print(solution(10, 85, 30))  # expected 3
