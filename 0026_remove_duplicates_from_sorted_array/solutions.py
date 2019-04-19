from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        nums_len = len(nums)
        while i != nums_len:
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                nums_len = len(nums)
            else:
                i = i + 1

        return len(nums)


nums = [1, 1, 2, 2, 3, 3, 3]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
