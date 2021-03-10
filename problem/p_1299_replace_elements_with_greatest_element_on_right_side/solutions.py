from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Runtime: 112 ms (97.69%)
        Memory Usage: 15.1 MB (98.06%)
        """
        if len(arr) == 1:
            return [-1]

        counter = len(arr) - 2
        origin_num, max_num = arr[-2], arr[-1]
        arr[-2], arr[-1] = arr[-1], -1

        while counter > 0:
            if origin_num > max_num:
                max_num = origin_num

            origin_num = arr[counter - 1]
            arr[counter - 1] = max_num

            counter -= 1
        return arr
