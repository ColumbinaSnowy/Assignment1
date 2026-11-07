# PermCheck (Codility Lesson 4 - Counting Elements)
# Time: O(N), Space: O(N)


def solution(A):
    N = len(A)
    seen = [False] * (N + 1)

    for value in A:
        # Value outside 1..N -> cannot be a permutation
        if value < 1 or value > N:
            return 0
        # Duplicate value -> cannot be a permutation
        if seen[value]:
            return 0
        seen[value] = True

    return 1
