class Solution(object):

    def mergeAlternately(self, word1, word2):
        mindex = min(len(word1), len(word2))
        return ''.join([''.join(i) for i in zip(word1, word2)]) + word1[mindex:] + word2[mindex:]



def try_test_case(word1, word2, expected):
    print(f"Trying test case {word1=}, {word2=}")
    s = Solution()
    output = s.mergeAlternately(word1, word2)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")


try_test_case("abc", "pqr", "apbqcr")
try_test_case("ab", "pqrs", "apbqrs")
try_test_case("abcd", "pq", "apbqcd")
