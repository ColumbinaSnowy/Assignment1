# PassingCars (Codility Lesson 5 - Prefix Sums)
# Time: O(N), Space: O(1)


def solution(A):
    total_pairs = 0
    east_cars_count = 0

    for car in A:
        if car == 0:
            # Car travelling east: keep track of it
            east_cars_count += 1
        else:
            # Car travelling west passes ALL previously seen east cars
            total_pairs += east_cars_count
            # Check if the count exceeds 1,000,000,000
            if total_pairs > 1000000000:
                return -1

    return total_pairs
