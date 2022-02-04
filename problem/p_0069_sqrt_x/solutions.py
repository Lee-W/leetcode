class Solution:
    """
    Runtime: 28 ms (97.81 %)
    Memory Usage: 14 MB (88 %)
    """

    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        elif x == 1:
            return 1

        start, end = 0, x - 1
        target = (start + end) // 2
        while start < end:
            if target * target > x:
                end = target - 1
            else:
                if (target + 1) * (target + 1) > x:
                    return target
                else:
                    start = target + 1

            target = (start + end) // 2

        return target
