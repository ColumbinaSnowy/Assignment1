# MaxCounters (Codility Lesson 4 - Counting Elements)
# Time: O(N + M), Space: O(N)


def solution(N, A):
    # N is the number of counters, A is the operations array
    counters = [0] * N

    # Variables to keep track of the minimum value and current max
    current_max = 0
    base_value = 0

    for X in A:
        if X == N + 1:
            # max counter: instead of updating all counters,
            # just record the new base value (lazy update)
            base_value = current_max
        else:
            # increase(X); index in array is X - 1 (0-indexed)
            index = X - 1

            # If the counter's actual value is less than the base value,
            # it hasn't been updated since the last max counter,
            # so set it to the base value and add 1.
            if counters[index] < base_value:
                counters[index] = base_value + 1
            else:
                counters[index] = counters[index] + 1

            # Update overall current maximum
            if counters[index] > current_max:
                current_max = counters[index]

    # Final pass to apply the base value to any counters left behind
    for i in range(N):
        if counters[i] < base_value:
            counters[i] = base_value

    return counters
