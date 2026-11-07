"""
Codility Lesson 4 (Counting Elements) - MaxCounters
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

There are N counters, all starting at 0. For each operation A[K]:
  - if 1 <= A[K] <= N : increase counter A[K] by 1
  - if A[K] == N + 1  : set every counter to the current maximum value
Return the final values of the counters.

Setting all N counters on every "max counter" operation would be O(N * M).
Instead we apply it lazily: remember the value every counter should have at
least (base) and only lift a counter up to that value when it is touched.

Time: O(N + M)   Space: O(N)
"""


def solution(N, A):
    counters = [0] * N
    base = 0         # value all counters were raised to by the last "max counter"
    current_max = 0  # highest counter value seen so far

    for op in A:
        if 1 <= op <= N:
            i = op - 1  # convert the 1-based counter number to a 0-based index
            # Apply any pending "max counter" to this counter before increasing it
            if counters[i] < base:
                counters[i] = base
            counters[i] += 1
            # Keep track of the largest counter value
            if counters[i] > current_max:
                current_max = counters[i]
        else:
            # op == N + 1: do not loop over all counters, just record the new base
            base = current_max

    # Counters never touched after the last "max counter" still need the base
    for i in range(N):
        if counters[i] < base:
            counters[i] = base

    return counters


if __name__ == "__main__":
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # expected [3, 2, 2, 4, 2]
