class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        

        freq= {}
        for elem in s:
            if elem in freq:
                freq[elem]+=1
            else:
                freq[elem]=1
    

        for elem in t:
            if elem not in freq:
                freq[elem] =1
            else:
                freq[elem] -=1
                if freq[elem]==0:
                    del freq[elem]
    
        
        print(freq)
        if freq != {}:
            return False
        else:
            return True
                    
            
            
            