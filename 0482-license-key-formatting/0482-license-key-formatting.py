class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        holderStack = []
        reverseStringArray = []
        kTemp = k
        for indx, char in enumerate(s):
            if char != "-":
                if char.isnumeric():
                    holderStack.append(char)
                else:
                    holderStack.append(char.upper())
        while holderStack:
            currentChar = holderStack.pop()
            if kTemp == 0:
                reverseStringArray.append("-")
                kTemp = k 
            reverseStringArray.append(currentChar)
            kTemp -= 1
        reverseStringArray.reverse()
        return "".join(reverseStringArray)

        