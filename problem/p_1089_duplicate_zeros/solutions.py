from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cur_index = 0
        while cur_index < len(arr):
            if arr[cur_index]:
                cur_index += 1
            else:
                arr.insert(cur_index, 0)
                cur_index += 2
                arr.pop()
