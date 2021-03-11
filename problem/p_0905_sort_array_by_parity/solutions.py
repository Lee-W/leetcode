from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Runtime: 72 ms (95.27%)
        Memory Usage: 14.8 MB (94.28 %)
        """
        r_pointer = len(A) - 1
        for left_pointer, a in enumerate(A):
            if left_pointer > r_pointer:
                break

            # odd number found by left_pointer
            if a % 2:
                while r_pointer > left_pointer and A[r_pointer] % 2:
                    r_pointer -= 1
                A[left_pointer], A[r_pointer] = A[r_pointer], A[left_pointer]
        return A
