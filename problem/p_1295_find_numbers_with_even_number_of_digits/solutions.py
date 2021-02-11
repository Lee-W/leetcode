from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            num_round = 0
            divided_num: float = num
            while divided_num >= 10:
                divided_num /= 10
                num_round += 1
            if num_round % 2:
                count += 1
        return count
