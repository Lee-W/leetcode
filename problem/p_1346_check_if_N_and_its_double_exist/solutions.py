from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for m_i, m in [(num_i, num) for num_i, num in enumerate(arr) if not num % 2]:
            for n_i, num in enumerate(arr):
                if m_i == n_i:
                    continue
                if num * 2 == m:
                    return True
        return False
