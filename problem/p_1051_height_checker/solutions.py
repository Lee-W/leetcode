from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Runtime: 28 ms (96.69 %)
        Memory Usage: 14.4 MB
        """
        # different_elements = [
        #     (x, y)
        #     for x, y in zip(heights, sorted(heights))
        #     if x != y
        # ]
        # return len(different_elements)
        return sum(1 for x, y in zip(heights, sorted(heights)) if x != y)
