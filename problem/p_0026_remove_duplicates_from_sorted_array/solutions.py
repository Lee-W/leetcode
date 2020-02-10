from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        nums_len = len(nums)
        while i != nums_len:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                nums_len = len(nums)
            else:
                i = i + 1

        return len(nums)
