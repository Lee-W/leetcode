# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num: int, pick: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


# on leetcode, guess and guessNumber only takes num argument
class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        start, end = 1, n

        target = (start + end) // 2
        while start < end:
            result = guess(target, pick)
            if result == 1:
                start = target + 1
            elif result == -1:
                end = target - 1
            else:
                return target
            target = (start + end) // 2

        return target
