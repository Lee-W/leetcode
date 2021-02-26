from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        while i != len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                continue

            i = i + 1

        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_len = 0
        for num_index, num in enumerate(nums[1:]):
            if nums[new_len] != num:
                new_len += 1
                nums[new_len] = num

        return new_len + 1
