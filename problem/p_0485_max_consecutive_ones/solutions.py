from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0

        for num in nums:
            if num:
                current_length += 1
            else:
                if current_length >= max_length:
                    max_length = current_length
                current_length = 0
        if current_length >= max_length:
            max_length = current_length
        return max_length
