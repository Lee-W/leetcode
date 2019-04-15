from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for sub_strs in zip(*strs):
            chr_set = set(sub_strs)
            if len(chr_set) > 1:
                break
            common_prefix += chr_set.pop()

        return common_prefix
