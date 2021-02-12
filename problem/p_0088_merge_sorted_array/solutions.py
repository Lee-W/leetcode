from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2[:]
            return

        count_1, count_2, count_origin, count_all_num = n, 0, 0, m + n
        nums1[n:] = nums1[:m]
        while count_1 < count_all_num and count_2 < n:
            if nums1[count_1] < nums2[count_2]:
                nums1[count_origin] = nums1[count_1]
                count_1 += 1
            else:
                nums1[count_origin] = nums2[count_2]
                count_2 += 1

            count_origin += 1

        if count_2 < n:
            nums1[count_origin:] = nums2[count_2:]
