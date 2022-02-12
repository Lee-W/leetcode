from typing import List


class Solution:
    """
    Runtime: 108 ms (89.08 %)
    Memory Usage: 14.4 MB (91.03 %)
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target:
            return letters[0]

        start, end = 0, len(letters) - 1

        mid = (start + end) // 2
        while start < end:
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2

        if letters[mid] > target:
            return letters[mid]

        if mid + 1 > len(letters) - 1:
            return letters[0]

        return letters[mid + 1]
