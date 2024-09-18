class Solution(object):

    def reverseVowels(self, s: str) -> str:
        vowel_indices = []
        vowel_values = []
        for (i, letter) in enumerate(s):
            if letter in "aeiouAEIOU":
                vowel_indices += [i]
                vowel_values += [letter]

        vowel_dict = dict(zip(vowel_indices, reversed(vowel_values)))

        return ''.join([s[i] if i not in vowel_dict else vowel_dict[i] for i in range(len(s)) ])

def try_test_case(s, expected):
    print(f"Trying test case {s=}")
    sol = Solution()
    output = sol.reverseVowels(s)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")
    return output == expected


if all(
    [
        try_test_case("hello", "holle"),
        try_test_case("leetcode", "leotcede"),
        try_test_case("asdf", "asdf"),
        try_test_case("eeoee", "eeoee"),
        try_test_case("f", "f"),
        try_test_case("a", "a"),
        try_test_case("", ""),
        try_test_case("leEtcodE", "lEotcEde"),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
