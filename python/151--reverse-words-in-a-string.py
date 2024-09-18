class Solution(object):

    def _alg1(self, s: str) -> str:
        """
        Solved simply using python builtins
        """
        return ' '.join(reversed(s.split()))

    def _reverse_in_place(self, l: list, left: int, right: int) -> None:
        assert left >= 0
        assert right <= len(l)

        while left < right:
            (l[left], l[right-1]) = (l[right-1], l[left])
            left += 1
            right -= 1

    def _alg2(self, s: str) -> str:
        """
        'In-place' solution.

        Developed after reviewing some optimal solutions.

        It's actually way slower than the simple solution. This is almost certainly
        because the actual builtin methods are c modules that are already pretty
        optimized.
        """
        s_list = list(s)
        s_list.reverse()  # Use builtin reverse because it works in place already

        i = 0
        left = 0
        right = 0

        while right < len(s_list) and s_list[right] == " ":
            right += 1

        while True:
            left = right
            while right < len(s_list) and s_list[right] != " ":
                right += 1
            self._reverse_in_place(s_list, left, right)
            while left < right:
                s_list[i] = s_list[left]
                left += 1
                i += 1

            while right < len(s_list) and s_list[right] == " ":
                right += 1

            if right >= len(s_list):
                break

            s_list[i] = " "
            i += 1

        return ''.join(s_list[:i])


    def reverseWords(self, s: str) -> str:
        return self._alg2(s)


def try_test_case(s, expected):
    print(f"Trying test case {s=}")
    sol = Solution()
    output = sol.reverseWords(s)
    print(f"  Output: |{output}|")
    print(f"  expected output: |{expected}|")
    print(f"  Passed? {output == expected}")
    return output == expected

if all(
    [
        try_test_case("the sky is blue", "blue is sky the"),
        try_test_case("  hello world  ", "world hello"),
        try_test_case("a good   example", "example good a"),
        try_test_case("  example      ", "example"),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
