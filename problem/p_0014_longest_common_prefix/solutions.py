from typing import List


class Solution:
    """
    Runtime: 55 ms (14.68%)
    Memory Usage: 14.3 MB (81.94%)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for sub_strs in zip(*strs):
            chr_set = set(sub_strs)
            if len(chr_set) > 1:
                break
            common_prefix += chr_set.pop()

        return common_prefix


class Solution2:
    """
    Runtime: 36 ms (62.35%)
    Memory Usage: 14.5 MB (24.95%)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        for c_idx, char in enumerate(first_str):
            for str_ in strs[1:]:
                if len(str_) < c_idx + 1 or str_[c_idx] != char:
                    return first_str[:c_idx]
        return first_str
