class Solution:

    def _alg1(self, s: str, t: str) ->bool:
        if len(s) > len(t):
            return False

        if s == "":
            return True

        j = 0
        for t_val in t:
            if s[j] == t_val:
                j += 1
            if j >= len(s):
                return True
        return False

    def run(self, s: str, t: str) -> bool:
        return self._alg1(s, t)


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
        try_test_case("abc", "ahbgdc", expected=True),
        try_test_case("axc", "ahbgdc", expected=False),
        try_test_case("abc", "abaaabababc", expected=True),
        try_test_case("a", "a", expected=True),
        try_test_case("b", "a", expected=False),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
