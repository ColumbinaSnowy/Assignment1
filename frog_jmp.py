# FrogJmp (Codility Lesson 3 - Time Complexity)
# Time: O(1), Space: O(1)


def solution(X, Y, D):
    # Calculate the total distance the frog needs to cover
    distance = Y - X

    # Calculate the minimum number of jumps using ceiling division
    # (integer arithmetic avoids floating-point rounding errors)
    jumps = (distance + D - 1) // D

    return jumps
