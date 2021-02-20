from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)


class Solution3:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        nums_len = len(nums)

        while nums_len > count:
            if nums[count] == val:
                nums[count] = nums[nums_len - 1]
                nums_len -= 1
                count -= 1
            count += 1
        return nums_len
