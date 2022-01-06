from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        Runtime: 60 ms (8.25 %)
        Memory Usage: 14.2 MB (73.27 %)
        """
        if len(nums) == 1:
            return 0

        max_num, max_index, second_max_num = nums[0], 0, 0
        for num_index, num in enumerate(nums[1:], 1):
            if num > max_num:
                max_index = num_index
                max_num, num = num, max_num

            if num > second_max_num:
                second_max_num = num

        return -1 if max_num / 2 < second_max_num else max_index
