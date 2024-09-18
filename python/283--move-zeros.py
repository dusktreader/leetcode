class Solution(object):

    def _alg1(self, nums: list[int]) -> None:
        """
        Original Solution.

        In-place.
        """
        zero_count = 0
        writer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writer] = nums[i]
                writer += 1
            else:
                zero_count += 1

        for i in range(zero_count):
            nums[writer] = 0
            writer += 1


    def moveZeros(self, nums: list[int]) -> None:
        return self._alg1(nums)


def try_test_case(nums, expected, expected_inplace=None):
    print(f"Trying test case {nums=}")
    sol = Solution()
    output = sol.moveZeros(nums)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    passed = output == expected

    if expected_inplace is not None:
        print(f"  In-place: {nums}")
        print(f"  expected in-place: {expected_inplace}")
        passed = passed and (nums == expected_inplace)

    print(f"  Passed? {passed}")
    return passed

if all(
    [
        try_test_case([0, 1, 0, 3, 12], None, expected_inplace=[1,3,12,0,0])
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
