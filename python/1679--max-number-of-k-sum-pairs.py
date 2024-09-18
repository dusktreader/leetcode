class Solution:
    def _alg1(self, nums: list[int], k:int) -> int:
        """
        Orignal solution.

        Apparently very slow. Only beats 5%... =[
        """
        counter = Counter(nums)
        ops_count = 0
        while len(counter) > 0:
            num = next(iter(counter))
            if num >= k:
                del counter[num]
                continue

            other_num = k - num
            if num == other_num:
                diff = counter[num] // 2
                del counter[num]
            else:
                other_num = k - num
                diff = min(counter[num], counter.get(other_num, 0))
                del counter[num]
                if diff > 0:
                    del counter[other_num]

            ops_count += diff
        return ops_count

    def _alg2(self, nums: list[int], k:int) -> int:
        """
        Re-implement without built-in counter.

        Still really slow. Only beats 16%
        """
        counter = dict()
        for num in nums:
            if num <= k:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1

        ops_count = 0
        while len(counter) > 0:
            num = next(iter(counter))
            other_num = k - num
            if num == other_num:
                diff = counter[num] // 2
                del counter[num]
            else:
                diff = min(counter[num], counter.get(other_num, 0))
                del counter[num]
                if diff > 0:
                    del counter[other_num]

            ops_count += diff
        return ops_count

    def _alg3(self, nums: list[int], k:int) -> int:
        """
        Two-pointer solution with sort.

        Borrowed from: https://leetcode.com/problems/max-number-of-k-sum-pairs/solutions/4363338/python-two-pointer-well-explain-solution-quick-and-still-mantain-o-1-space-complexity

        Should be much slower since my original solution is O(n) and this will be O(nlogn).

        This some bullshit...now it beats 79%.
        """
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            lr = sorted_nums[left] + sorted_nums[right]
            if lr == k:
                ops += 1
                left += 1
                right -= 1
            elif lr < k:
                left += 1
            else:
                right -= 1

        return ops

    def run(self, *args) -> int:
        return self._alg3(*args)


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
        try_test_case([1,2,3,4], 5, expected=2),
        try_test_case([3,1,3,4,3], 6, expected=1),
        try_test_case([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2, expected=2),
    ]
):
    print("All tests pass!")
else:
    print("Some tests failed")
