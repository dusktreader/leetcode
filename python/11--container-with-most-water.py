class Solution:
    def _alg1(self, height: list[int]) -> int:
        """
        Original solution.
        """
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if max_left > max_right:
                right -= 1
            else:
                left += 1
        return max_area

    def _alg2(self, height: list[int]) -> int:
        """
        Based on answer: https://leetcode.com/problems/container-with-most-water/solutions/6100/simple-and-clear-proof-explanation

        Removes extra max calculations for left and right.
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area

    def run(self, *args) -> int:
        return self._alg1(*args)


def try_test_case(*args, expected=None):
    print(f"Trying test case for {args=}")
    print(f"  with {expected=}")
    sol = Solution()
    result = sol.run(*args)
    print(f"  {result=}")
    passed = expected == result
    print(f"  {passed=}")
    return passed

if all(
    [
        try_test_case([1,8,6,2,5,4,8,3,7], expected=49),
        try_test_case([2,3,4,5,18,17,6], expected=17),
    ]
):
    print("All tests pass!")
else:
    print("Some tests failed")
