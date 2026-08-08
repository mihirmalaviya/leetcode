class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        odd=0
        res=0
        for _,v in Counter(s).items():
            if not odd and v%2:
                odd+=1
            res+=v-v%2
            
        res+=odd
        return res
            
            

