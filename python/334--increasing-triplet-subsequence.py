class Solution(object):

    def _alg1(self, nums: list[int]) -> bool:
        """
        Brute Force
        """
        if len(nums) < 3:
            return False

        i = 0

        while True:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
                    k += 1
                j += 1
            i += 1

            if i >= len(nums) - 2:
                break

        return False

    def _alg1(self, nums: list[int]) -> bool:
        """
        left/mid

        Copied from: https://leetcode.com/problems/increasing-triplet-subsequence/solutions/2688292/c-easy-and-simple-o-n-time-and-o-1-space/?envType=study-plan-v2&envId=leetcode-75
        """
        if len(nums) < 3:
            return False

        int_max = int(2**31 - 1)

        left = int_max
        mid = int_max

        for val in nums:
            if val > mid:
                return True
            elif val > left and val < mid:
                mid = val
            elif val < left:
                left = val

        return False

    def increasingTriplet(self, nums: list[int]) -> bool:
        return self._alg1(nums)


def try_test_case(nums, expected):
    print(f"Trying test case {nums=}")
    sol = Solution()
    output = sol.increasingTriplet(nums)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")
    return output == expected

if all(
    [
        try_test_case([1,2,3,4,5], True),
        try_test_case([5,4,3,2,1], False),
        try_test_case([2,1,5,0,4,6], True),
        try_test_case([1,5,0,4,1,3], True),
        try_test_case([20, 100, 10, 12, 5, 13], True),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
