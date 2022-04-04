from typing import List


class Solution:
    """
    Runtime: 395 ms (88.87 %)
    Memory Usage: : 21.9 MB (47.86 %)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


class Solution2:
    """
    Runtime: 819 ms (60.03 %)
    Memory Usage: : 22.5 MB (34.72 %)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        left = self.sortArray(nums[len(nums) // 2 :])
        right = self.sortArray(nums[: len(nums) // 2])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]):
        left_cursor, right_cursor = 0, 0
        result = []

        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] > right[right_cursor]:
                result.append(right[right_cursor])
                right_cursor += 1
            else:
                result.append(left[left_cursor])
                left_cursor += 1

        result.extend(left[left_cursor:])
        result.extend(right[right_cursor:])

        return result
