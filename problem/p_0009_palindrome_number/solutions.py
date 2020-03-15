class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        x_str = str(x)
        middle = int(len(x_str) / 2)
        for i, j in zip(x_str[: middle + 1 : 1], x_str[: middle - 1 : -1]):
            if i != j:
                return False
        return True
