class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0

        h_len, n_len = len(haystack), len(needle)
        if n_len > h_len:
            return -1

        for i, c in enumerate(haystack):
            if c == needle[0] and (h_len - i >= n_len):
                if haystack[i : i + n_len] == needle:
                    return i

        return -1
