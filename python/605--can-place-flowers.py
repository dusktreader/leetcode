class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True

        if flowerbed == [0] and n == 1:
            return True

        count = 0

        if flowerbed[:2] == [0, 0]:
            count += 1
            if count >= n:
                return True
            i = 2
        else:
            i = 1

        while i < len(flowerbed) - 1:
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1
            if count >= n:
                return True

        if flowerbed[i-1:len(flowerbed)] == [0, 0]:
            count += 1
            if count >= n:
                return True

        return False





def try_test_case(flowerbed, n, expected):
    print(f"Trying test case {flowerbed=}, {n=}")
    s = Solution()
    output = s.canPlaceFlowers(flowerbed, n)
    print(f"  Output: {output}")
    print(f"  expected output: {expected}")
    print(f"  Passed? {output == expected}")
    return output == expected


if all(
    [
        try_test_case([1,0,0,0,1], 1, True),
        try_test_case([1,0,0,0,1], 2, False),
        try_test_case([0,0,1,0,1], 1, True),
        try_test_case([1,0,0,0,1,0,0], 2, True),
        try_test_case([1,0,0,1,0,0,0], 2, False),
        try_test_case([1], 0, True),
        try_test_case([0], 1, True),
    ]
):
    print("All tests passed!")
else:
    print("Some tests failed!")
