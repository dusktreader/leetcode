class Solution(object):

    def _alg1(self, chars: list[str]) -> int:
        """
        Original solution.

        Everything in-place.

        Complexity: O(n)
        Space complexity (extra): O(1)
        """
        n = len(chars)
        if n == 1:
            return 1

        writer: int = 0
        left: int = 0
        right: int = 1
        while True:
            if right >= n or chars[left] != chars[right]:
                chars[writer] = chars[left]
                writer += 1
                if right - left > 1:
                    for digit in str(right - left):
                        chars[writer] = digit
                        writer += 1
                left = right
            if right >= n:
                break
            right += 1
        del chars[writer:]
        return writer


    def compress(self, chars: list[str]) -> int:
        return self._alg1(chars)


def try_test_case(chars, expected, expected_inplace=None):
    print(f"Trying test case {chars=}")
    sol = Solution()
    output = sol.compress(chars)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    passed = output == expected

    if expected_inplace is not None:
        print(f"  In-place: {chars}")
        print(f"  expected in-place: {expected_inplace}")
        passed = passed and (chars == expected_inplace)

    print(f"  Passed? {passed}")
    return passed

if all(
    [
        try_test_case(["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"]),
        try_test_case(["a"], 1, ["a"]),
        try_test_case(["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4, ["a", "b", "1", "2"]),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
