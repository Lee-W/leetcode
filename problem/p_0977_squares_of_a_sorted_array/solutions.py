from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r_cur = -1
        for num_index, num in enumerate(nums):
            if num >= 0:
                r_cur = num_index
                break

        if r_cur == -1:
            return [num ** 2 for num in nums[::-1]]
        elif not r_cur:
            return [num ** 2 for num in nums]

        results = []
        l_cur = r_cur - 1
        while l_cur > -1 and r_cur < len(nums):
            if -nums[l_cur] < nums[r_cur]:
                results.append(nums[l_cur])
                l_cur -= 1
            else:
                results.append(nums[r_cur])
                r_cur += 1
        if l_cur > -1:
            for num in nums[l_cur::-1]:
                results.append(num)
        elif r_cur < len(nums):
            for num in nums[r_cur:]:
                results.append(num)
        return [num ** 2 for num in results]
