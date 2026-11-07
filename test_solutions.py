"""Tests for the five solutions: examples from Codility, edge cases,
and random comparisons against simple brute-force versions."""
import random
import unittest

import frog_jmp
import max_counters
import missing_integer
import passing_cars
import perm_check


class TestFrogJmp(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(frog_jmp.solution(10, 85, 30), 3)
        self.assertEqual(frog_jmp.solution(10, 10, 5), 0)   # already there
        self.assertEqual(frog_jmp.solution(10, 70, 30), 2)  # exact multiple
        self.assertEqual(frog_jmp.solution(1, 1_000_000_000, 1), 999_999_999)


class TestPermCheck(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(perm_check.solution([4, 1, 3, 2]), 1)
        self.assertEqual(perm_check.solution([4, 1, 3]), 0)
        self.assertEqual(perm_check.solution([1]), 1)
        self.assertEqual(perm_check.solution([2]), 0)
        self.assertEqual(perm_check.solution([1, 1]), 0)


class TestMissingInteger(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(missing_integer.solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(missing_integer.solution([1, 2, 3]), 4)
        self.assertEqual(missing_integer.solution([-1, -3]), 1)
        self.assertEqual(missing_integer.solution([1_000_000]), 1)

    def test_random(self):
        for _ in range(500):
            a = [random.randint(-5, 15) for _ in range(random.randint(1, 12))]
            expected = next(k for k in range(1, 100) if k not in a)
            self.assertEqual(missing_integer.solution(a), expected)


class TestMaxCounters(unittest.TestCase):
    def test_example(self):
        self.assertEqual(max_counters.solution(5, [3, 4, 4, 6, 1, 4, 4]),
                         [3, 2, 2, 4, 2])

    def test_random(self):
        for _ in range(500):
            n = random.randint(1, 6)
            ops = [random.randint(1, n + 1) for _ in range(random.randint(1, 20))]
            expected = [0] * n
            for op in ops:  # brute force
                if op <= n:
                    expected[op - 1] += 1
                else:
                    expected = [max(expected)] * n
            self.assertEqual(max_counters.solution(n, ops), expected)


class TestPassingCars(unittest.TestCase):
    def test_example(self):
        self.assertEqual(passing_cars.solution([0, 1, 0, 1, 1]), 5)

    def test_limit(self):
        self.assertEqual(passing_cars.solution([0] * 50_000 + [1] * 50_000), -1)
        # 40,000 * 25,000 = 1,000,000,000 exactly -> still allowed
        self.assertEqual(passing_cars.solution([0] * 40_000 + [1] * 25_000),
                         1_000_000_000)

    def test_random(self):
        for _ in range(500):
            a = [random.randint(0, 1) for _ in range(random.randint(1, 15))]
            expected = sum(1 for p in range(len(a)) for q in range(p + 1, len(a))
                           if a[p] == 0 and a[q] == 1)
            self.assertEqual(passing_cars.solution(a), expected)


if __name__ == "__main__":
    unittest.main()
