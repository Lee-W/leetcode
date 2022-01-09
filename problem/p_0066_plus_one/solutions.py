from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Runtime: 38 ms (26.52 %)
        Memory Usage: 14.1 MB (76.04 %)
        """
        for d_idx in range(len(digits) - 1, -1, -1):
            if digits[d_idx] != 9:
                digits[d_idx] += 1
                break
            else:
                digits[d_idx] = 0

        if not digits[0]:
            digits.insert(0, 1)

        return digits
