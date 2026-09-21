class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)

            elif char in ")}]":
                if not stack:
                    return False

                opening = stack.pop()

                if (char == ')' and opening != '(') or \
                   (char == '}' and opening != '{') or \
                   (char == ']' and opening != '['):
                    return False

        return not stack




        