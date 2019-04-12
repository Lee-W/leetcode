class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        x = str(x)
        middle = int(len(x)/2)
        for i, j in zip(x[:middle+1:1], x[:middle-1:-1]):
            if i != j:
                return False
        return True
