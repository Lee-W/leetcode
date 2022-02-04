from typing import List


class Solution:
    """
    Runtime: 248 ms (59.90 %)
    Memory Usage: 15.5 MB (90.45 %)
    """

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            search_index = (start + end) // 2
            if target == nums[search_index]:
                return search_index
            elif target > nums[search_index]:
                start = search_index + 1
            else:
                end = search_index - 1

        return -1
