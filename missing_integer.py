# MissingInteger (Codility Lesson 4 - Counting Elements)
# Time: O(N), Space: O(N)


def solution(A):
    # n is the length of array A
    n = len(A)

    # Boolean array to keep track of seen numbers
    # Size n + 2 so we can safely access index up to n + 1
    seen = [False] * (n + 2)

    # Mark every positive integer within the range 1..n
    for x in A:
        if 1 <= x <= n:
            seen[x] = True

    # Iterate from 1 to n + 1 to find the smallest missing positive integer
    for i in range(1, n + 2):
        if not seen[i]:
            return i

    # Fallback, though the loop above will always return
    return n + 1
