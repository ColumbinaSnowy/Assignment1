"""
Codility Lesson 5 (Prefix Sums) - PassingCars
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

A[i] == 0 means a car travelling east, A[i] == 1 a car travelling west.
A pair (P, Q) with 0 <= P < Q < N is passing when A[P] == 0 and A[Q] == 1.
Return the number of passing pairs, or -1 if it exceeds 1,000,000,000.

Time: O(N)   Space: O(1)
"""

LIMIT = 1_000_000_000


def solution(A):
    east_count = 0  # number of east-bound cars seen so far (to the left)
    passing = 0     # number of passing pairs found

    for car in A:
        if car == 0:
            # An east-bound car will pass every west-bound car to its right
            east_count += 1
        else:
            # A west-bound car is passed by every east-bound car to its left
            passing += east_count
            # Stop early once the result is too large
            if passing > LIMIT:
                return -1

    return passing


if __name__ == "__main__":
    print(solution([0, 1, 0, 1, 1]))  # expected 5
