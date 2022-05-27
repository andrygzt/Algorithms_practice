'''
DESCRIPTION
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq={}
        for elem in s:
            if elem in freq:
                freq[elem]+=1
            else:
                freq[elem]=1
        
        
        for elems in t:
            if elems not in freq:
                return False
            elif elems in freq:
                if freq[elems]<=0:
                    return False
                else:
                    freq[elems]-=1 
        return True

s="aacc"
t="ccac"
sol=Solution()
sol.isAnagram(s,t)
#printing solution
print(sol.isAnagram(s,t))





'''
Mi first attempt to solution gives:
Runtime: 75 ms
Memory Usage: 14.4 MB
Because of the use of .keys() built in function inside of the for loop.
See details here ---> https://leetcode.com/submissions/detail/708125685/


My best version performs:
Runtime: 59 ms
Memory Usage: 14.6 MB
This time I deleted the use of build in functions inside the loop.
See details here ---> https://leetcode.com/submissions/detail/708128742/

'''


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq={}
        freq2={}
        for elem in s:
            if elem in freq:
                freq[elem]+=1
            else:
                freq[elem]=1
        
        for eleme in t:
            if eleme in freq2:
                freq2[eleme]+=1
            else:
                freq2[eleme]=1
        
        if freq.items()==freq2.items():
            return True
        else:
            return False

s="aacc"
t="cacc"
sol=Solution1()
sol.isAnagram(s,t)
#printing solution
print(sol.isAnagram(s,t))

'''
Mi first attempt to solution gives:
Runtime: 51 ms
Memory Usage: 14.4 MB
Because of the use of .keys() built in function inside of the for loop.
See details here ---> https://leetcode.com/submissions/detail/708142433/
In this time it seems that the use of build in .items() makes this solution more efficient.


My best version performs:
Runtime: 53 ms
Memory Usage: 14.5 MB
This time I deleted the use of build in functions inside the loop.
See details here ---> https://leetcode.com/submissions/detail/708145076/

'''

