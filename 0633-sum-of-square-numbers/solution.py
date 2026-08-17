class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l=0
        r=int(c**.5)

        while l<=r:
            x=l**2+r**2
            if x==c:
                return True
            elif x>c:
                r-=1
            else:
                l+=1

        return False
