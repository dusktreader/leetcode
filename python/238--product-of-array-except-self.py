class Solution(object):

    def _alg1(self, nums: list[int]) -> list[int]:
        """
        Brute force
        """
        new_nums = [1] * len(nums)
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j:
                    new_nums[i] *= nums[j]
                j += 1
            i += 1
        return new_nums

    def _alg2(self, nums: list[int]) -> list[int]:
        """
        Minimal space complexity.
        """
        n = len(nums)
        zero_index = None
        new_nums = [0] * n

        # Zero scan
        for i in range(n):
            if nums[i] == 0:
                if zero_index is not None:
                    return new_nums
                zero_index = i

        total_product = 1
        # Product scan
        for i in range(n):
            if i == zero_index:
                continue
            total_product *= nums[i]

        if zero_index is not None:
            new_nums[zero_index] = total_product
            return new_nums

        # Final divide scan
        for i in range(n):
            new_nums[i] = total_product // nums[i]

        return new_nums

    def _alg3(self, nums: list[int]) -> list[int]:
        """
        Using left/right array produts.

        Written after reviewing answers on leetcode.
        It's actually way slower than _alg2
        """
        n = len(nums)
        new_nums = [1] * n
        left_prod = [1] * n
        right_prod = [1] * n


        # Left Scan
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        # Right scan
        for i in range(n-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        print(f"{left_prod=}")
        print(f"{right_prod=}")

        # Final scan
        for i in range(n):
            new_nums[i] = left_prod[i] * right_prod[i]

        return new_nums


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return self._alg3(nums)


def try_test_case(nums, expected):
    print(f"Trying test case {nums=}")
    sol = Solution()
    output = sol.productExceptSelf(nums)
    print(f"  Output: |{output}|")
    print(f"  expected output: |{expected}|")
    print(f"  Passed? {output == expected}")
    return output == expected

if all(
    [
        try_test_case([1,2,3,4], [24, 12, 8, 6]),
        try_test_case([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        try_test_case([1, 0, 2, 0, 3], [0, 0, 0, 0, 0]),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
