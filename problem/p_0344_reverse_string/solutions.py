from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Runtime: 208 ms (45.91%)
        Memory Usage: 18.7 MB (19.11%)
        Do not return anything, modify s in-place instead.
        """
        for c_idx in range(len(s) // 2):
            r_idx = len(s) - 1 - c_idx
            s[c_idx], s[r_idx] = s[r_idx], s[c_idx]


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Runtime: 192 ms, faster than 92.35%
        Memory Usage: 18.6 MB, less than 44.89%

        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
