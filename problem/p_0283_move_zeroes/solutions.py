from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Runtime: 36 ms (99.75%)
        Memory Usage: 15.4 MB (64.36%)

        Do not return anything, modify nums in-place instead.
        """
        new_len = 0
        for num in nums:
            if num:
                nums[new_len] = num
                new_len += 1

        nums[new_len:] = [0] * (len(nums) - new_len)
