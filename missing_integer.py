"""
Codility Lesson 4 (Counting Elements) - MissingInteger
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

Return the smallest positive integer (greater than 0) that does not occur in A.

Time: O(N)   Space: O(N)
"""


def solution(A):
    n = len(A)
    # The answer is always in the range 1..N+1:
    # with only N numbers, at least one of 1..N+1 must be missing.
    # present[v] is True if v (1 <= v <= N+1) appears in A.
    present = [False] * (n + 2)

    for value in A:
        # Ignore non-positive numbers and numbers too big to matter
        if 1 <= value <= n + 1:
            present[value] = True

    # The first value not marked as present is the answer
    for candidate in range(1, n + 2):
        if not present[candidate]:
            return candidate

    return n + 2  # never reached, kept as a safe fallback


if __name__ == "__main__":
    print(solution([1, 3, 6, 4, 1, 2]))  # expected 5
    print(solution([1, 2, 3]))           # expected 4
    print(solution([-1, -3]))            # expected 1
