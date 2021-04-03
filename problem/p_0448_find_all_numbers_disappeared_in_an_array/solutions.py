from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Runtime: 352 ms (59.79 %)
        Memory Usage: 25.2 MB (20.22 %)
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Runtime: 488 ms
        Memory Usage: 21.4 MB (98.29 %)
        """
        for num_index, num in enumerate(nums):
            correct_loc = num - 1
            while num_index != correct_loc:
                num_2 = nums[correct_loc]
                nums[correct_loc] = num

                num_index = correct_loc
                num = num_2
                correct_loc = num - 1
        return [num_index for num_index, num in enumerate(nums, 1) if num != num_index]
