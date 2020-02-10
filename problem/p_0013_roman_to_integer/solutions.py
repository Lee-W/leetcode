class Solution:
    SYMBOL_TO_VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return self.SYMBOL_TO_VALUE[s]

        digits = [self.SYMBOL_TO_VALUE[c] for c in s]

        value = 0
        for d1, d2 in zip(digits[:-1], digits[1:]):
            if d2 > d1:
                value -= d1
            else:
                value += d1

        if d2:
            value += d2
        return value
