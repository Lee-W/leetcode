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
    BRACKET_MAPPING = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

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
