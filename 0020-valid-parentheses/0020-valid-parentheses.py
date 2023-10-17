class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {"{": "}", "(": ")", "[": "]"}

        for item in s:

            if item in pairs:
                closingSymbol = pairs[item] 
                stack.append(closingSymbol)
            elif len(stack) == 0:
                return False
            elif item != stack.pop():
                return False

        if len(stack) != 0:
            return False

        return True
