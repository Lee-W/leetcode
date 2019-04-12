class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -int(str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])

        if 2**31 > x > -2**31 -1:
            return x
        return 0
