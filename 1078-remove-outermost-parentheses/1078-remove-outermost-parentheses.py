class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if len(s)%2 != 0:
            return ""

        popen, result = 0, []
        for char  in s:
            if char ==')':
                popen -= 1
            if popen>0:
                result.append(char)
            if char =='(':
                popen += 1
        return ''.join(result)