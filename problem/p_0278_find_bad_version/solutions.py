# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(version: int, bad: int) -> bool:
    # The bad argument is not passed in the following function / method on leetcode
    return version >= bad


class Solution:
    """
    Runtime: 28 ms (88.83 %)
    Memory Usage: 13.8 MB (99.68 %)
    """

    def firstBadVersion(self, n: int, bad: int) -> int:
        start = 1

        target = (start + n) // 2
        while start < n:
            if isBadVersion(target, bad):
                if isBadVersion(target - 1, bad):
                    n = target - 1
                else:
                    return target
            else:
                start = target + 1
            target = (start + n) // 2

        return target
