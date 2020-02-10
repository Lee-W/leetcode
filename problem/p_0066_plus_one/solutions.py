from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_index = len(digits) - 1

        while digits[current_index] == 9 and current_index > 0:
            digits[current_index] = 0
            current_index -= 1

        if digits[current_index] == 9 and current_index == 0:
            digits[current_index] = 0
            digits.insert(0, 1)
        else:
            digits[current_index] += 1

        return digits
