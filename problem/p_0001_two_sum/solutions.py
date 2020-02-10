from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_values = [target - num for num in nums]

        for num_index, num in enumerate(nums):
            if num in remain_values:
                remain_index = remain_values.index(num)

                if num_index != remain_index:
                    return [num_index, remain_index]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_index, num in enumerate(nums):
            remain = target - num

            if remain in nums:
                remain_index = nums.index(remain)
                if remain_index != num_index:
                    return [num_index, remain_index]
