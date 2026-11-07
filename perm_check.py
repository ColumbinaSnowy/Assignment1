"""
Codility Lesson 4 (Counting Elements) - PermCheck
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

Return 1 if array A (length N) is a permutation of 1..N, otherwise 0.

Time: O(N)   Space: O(N)
"""


def solution(A):
    n = len(A)
    # seen[v] becomes True once value v has appeared (index 0 is unused)
    seen = [False] * (n + 1)

    for value in A:
        # A value outside 1..N can never be part of a permutation of 1..N
        if value < 1 or value > n:
            return 0
        # A repeated value means some other value in 1..N must be missing
        if seen[value]:
            return 0
        seen[value] = True

    # N values, all in range 1..N and all distinct -> every value appears once
    return 1


if __name__ == "__main__":
    print(solution([4, 1, 3, 2]))  # expected 1
    print(solution([4, 1, 3]))     # expected 0
