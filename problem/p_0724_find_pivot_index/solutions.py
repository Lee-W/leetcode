from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Runtime: 142 ms (88.45%)
        Memory Usage: 15.5 MB (40.33%)
        """
        left_sum = 0
        right_sum = sum(nums[1:])  # O(n-1)

        if not right_sum:
            return 0

        for num_index, num in enumerate(nums[1:], 1):
            left_sum += nums[num_index - 1]
            right_sum -= num

            if left_sum == right_sum:
                return num_index
        return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Runtime: 298 ms (15.32%)
        Memory Usage: 15.5 MB (40.33%)
        """
        pivot_index = 0
        left_sum = nums.pop(0)  # second round
        right_sum = sum(nums)  # first round

        if not right_sum:
            return 0

        while nums:
            num = nums.pop(0)
            pivot_index += 1

            right_sum -= num
            if left_sum == right_sum:
                return pivot_index

            left_sum += num
        return -1
