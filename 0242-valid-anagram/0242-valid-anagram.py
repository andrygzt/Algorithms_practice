class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        def helper(a):
            freq= {}
            for elem in a:
                if elem in freq:
                    freq[elem]+=1
                else:
                    freq[elem]=1
            return freq
        
        
        if helper(s) == helper(t):
            return True
        else:
            return False
                    
            
            
            