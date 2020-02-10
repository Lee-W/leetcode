class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        for r_index, sub_s in enumerate(s[::-1]):
            if sub_s == " ":
                return r_index
        else:
            return len(s)
        return 0
