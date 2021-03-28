from typing import List, Optional


class Solution:
    def thirdMax(self, nums: List[int]) -> Optional[int]:
        """
        Runtime: 1380 ms
        Memory Usage: 15.2 MB (73.02 %)
        """
        max_three_nums: List[Optional[int]] = [nums[0], None, None]

        for num in nums[1:]:
            for max_index, max_num in enumerate(max_three_nums):
                if num == max_num:
                    break

                if not max_num:
                    max_three_nums[max_index] = num
                    break

                if num > max_num:
                    max_three_nums.insert(max_index, num)
                    break

        return max_three_nums[0] if max_three_nums[2] is None else max_three_nums[2]


class Solution2:
    def thirdMax(self, nums: List[int]) -> Optional[int]:
        """
        Runtime: 44 ms (96.25 %)
        Memory Usage: 15.8 MB (26.71 %)
        """
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[0] if len(nums) < 3 else nums[2]
