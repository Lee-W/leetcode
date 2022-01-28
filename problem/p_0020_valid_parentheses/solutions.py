class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = list()
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)

            if c in (")", "]", "}"):
                if not stack:
                    return False

                top = stack.pop()
                # {: 123, }: 125, (: 40, ): 41, [: 91, ]:93
                if abs(ord(c) - ord(top)) > 2:
                    return False

        if stack:
            return False
        return True


class Solution2:
    BRACKET_MAPPING = {"{": "}", "(": ")", "[": "]"}

    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = list()
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)

            if c in (")", "]", "}"):
                if not stack:
                    return False

                top = stack.pop()
                if self.BRACKET_MAPPING[top] != c:
                    return False

        if stack:
            return False

        return True


class Solution3:
    """
    Runtime: 24 ms (97.37 %)
    Memory Usage: 13.9 MB (99.8 %)
    """

    def isValid(self, s: str) -> bool:
        parenthese_mappging = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for c in s:
            if c in parenthese_mappging:
                stack.append(c)
            else:
                if stack and parenthese_mappging[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        return not bool(stack)
