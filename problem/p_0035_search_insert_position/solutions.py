from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0

        for n_index, num in enumerate(nums):
            if target <= num:
                return n_index
        return len(nums)
