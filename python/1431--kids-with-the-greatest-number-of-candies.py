class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [k + extraCandies >= max_candies for k in candies]


def try_test_case(candies, extraCandies, expected):
    print(f"Trying test case {candies=}, {extraCandies=}")
    s = Solution()
    output = s.kidsWithCandies(candies, extraCandies)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")


try_test_case([2, 3, 5, 1, 3], 3, [True, True, True, False, True])
try_test_case([4, 2, 1, 1, 2], 1, [True, False, False, False, False])
try_test_case([12, 1, 12], 10, [True, False, True])
