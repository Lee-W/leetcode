class Solution:
    """
    Runtime: 32 ms (77.7 %)
    Memory Usage: 13.9 MB (94.25 %)
    """

    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num

        target = (start + end) // 2
        while start <= end:
            if target ** 2 == num:
                return True
            elif target ** 2 > num:
                end = target - 1
            else:
                start = target + 1

            target = (start + end) // 2
        return False
