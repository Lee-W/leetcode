from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Runtime: 188 ms (98.08%)
        Memory Usage: 15.5 MB (55.28%)
        """
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False

        is_decreasing = False
        for num_i, num in enumerate(arr[0:-2]):
            num_2 = arr[num_i + 1]
            if not is_decreasing:
                if num > num_2:
                    is_decreasing = True
                elif num == num_2:
                    return False
            else:
                if not num > num_2:
                    return False
        return True
