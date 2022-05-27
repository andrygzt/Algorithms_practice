'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s=s.reverse()

'''
Mi first attempt to solution gives:
Runtime: 300 ms
Memory Usage: 18.7 MB
See details here ---> https://leetcode.com/submissions/detail/708191294/


My best version performs:
Runtime: 270 ms
Memory Usage: 18.3 MB
Using al build in function is considerable more efficient.
See details here ---> https://leetcode.com/submissions/detail/708192747/

'''
