class Solution:
    def _alg1(self, nums: list[int], k: int) -> float:
        """
        Original solution.

        time complexity => O(n)
        space complexity (additional) => O(1)
        """
        curr_sum = sum(nums[:k])
        max_avg = curr_sum / k
        for i in range(len(nums) - k):
            curr_sum = curr_sum - nums[i] + nums[i + k]
            max_avg = max(max_avg, curr_sum / k)
        return max_avg

    def _alg2(self, nums: list[int], k: int) -> float:
        """
        Optimized solution.

        Removed repeated division to find average and moved it to the end only.
        Borrowed from: https://leetcode.com/problems/maximum-average-subarray-i/solutions/3799916/java-100-faster-solution-sliding-window
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(len(nums) - k):
            curr_sum = curr_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k

    def run(self, *args) -> float:
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
        try_test_case([1, 12, -5, -6, 50, 4], 4, expected=12.75),
        try_test_case([5], 1, expected=5.0),
    ]
):
    print("All tests pass!")
else:
    print("Some tests failed")
