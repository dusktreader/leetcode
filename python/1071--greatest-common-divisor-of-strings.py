class Solution(object):

    def _is_divisor(self, d, word):
        if len(word) % len(d) != 0:
            return False
        m = len(word) // len(d)
        if d * m == word:
            return True
        return False

    def _alg1(self, str1, str2):
        gcd = ""
        gcd_len = min(len(str1), len(str2))
        while gcd_len > 0:
            substring = str1[:gcd_len]
            if substring == str2[:gcd_len] and self._is_divisor(substring, str1) and self._is_divisor(substring, str2):
                gcd = substring
            gcd_len -= 1
        return gcd

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        return self._alg1(str1, str2)


def try_test_case(str1, str2, expected):
    print(f"Trying test case {str1=}, {str2=}")
    s = Solution()
    output = s.gcdOfStrings(str1, str2)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")


try_test_case("ABCABC", "ABC", "ABC")
try_test_case("ABABAB", "ABAB", "AB")
try_test_case("LEET", "CODE", "")
