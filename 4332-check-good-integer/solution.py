class Solution:
    def checkGoodInteger(self, n: int) -> bool:


        res=0
        digits=[int(ch) for ch in str(n)]
        for digit in digits:
            res+= digit**2-digit
            
        return res>=50
