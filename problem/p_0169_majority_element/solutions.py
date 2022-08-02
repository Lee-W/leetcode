from typing import List
from collections import Counter


class Solution:
    """
    Runtime: 188 ms (82.93 %)
    Memory Usage: 15.5 MB (86.37 %)
    """

    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        max_count = 0
        majority_element = -1

        for num in nums:
            if num not in counter:
                counter[num] = 0

            counter[num] += 1

            if counter[num] > max_count:
                max_count = counter[num]
                majority_element = num

        return majority_element


class Solution2:
    """
    Runtime: 255 ms (67.59 %)
    Memory Usage: 15.6 MB (35.03 %)
    """

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
