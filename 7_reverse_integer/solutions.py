class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        positive_x_str = str(abs(x))

        if is_negative:
            result = -int(positive_x_str[::-1])
        else:
            result = int(positive_x_str[::-1])

        if 2**31 > result > -2**31 -1:
            return result
        return 0
